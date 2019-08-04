from requests import Session
from dangdangbook.config import *
from dangdangbook.redisqueue import RedisQueue
from dangdangbook.request import DangdangRequest
from urllib.parse import urlencode

from requests import ReadTimeout, ConnectionError
from bs4 import BeautifulSoup
from dangdangbook.savetoexcel import Saver


class Spider(object):
    base_url = 'http://search.dangdang.com'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'IPLOC=CN1100; SUID=6FEDCF3C541C940A000000005968CF55; SUV=1500041046435211; ABTEST=0|1500041048|v1; SNUID=CEA85AE02A2F7E6EAFF9C1FE2ABEBE6F; weixinIndexVisited=1; JSESSIONID=aaar_m7LEIW-jg_gikPZv; ld=Wkllllllll2BzGMVlllllVOo8cUlllll5G@HbZllll9lllllRklll5@@@@@@@@@@; LSTMV=212%2C350; LCLKINT=4650; ppinf=5|1500042908|1501252508|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1NDolRTUlQjQlOTQlRTUlQkElODYlRTYlODklOEQlRTQlQjglQTglRTklOUQlOTklRTglQTclODV8Y3J0OjEwOjE1MDAwNDI5MDh8cmVmbmljazo1NDolRTUlQjQlOTQlRTUlQkElODYlRTYlODklOEQlRTQlQjglQTglRTklOUQlOTklRTglQTclODV8dXNlcmlkOjQ0Om85dDJsdUJfZWVYOGRqSjRKN0xhNlBta0RJODRAd2VpeGluLnNvaHUuY29tfA; pprdig=ppyIobo4mP_ZElYXXmRTeo2q9iFgeoQ87PshihQfB2nvgsCz4FdOf-kirUuntLHKTQbgRuXdwQWT6qW-CY_ax5VDgDEdeZR7I2eIDprve43ou5ZvR0tDBlqrPNJvC0yGhQ2dZI3RqOQ3y1VialHsFnmTiHTv7TWxjliTSZJI_Bc; sgid=27-27790591-AVlo1pzPiad6EVQdGDbmwnvM; PHPSESSID=mkp3erf0uqe9ugjg8os7v1e957; SUIR=CEA85AE02A2F7E6EAFF9C1FE2ABEBE6F; sct=11; ppmdig=1500046378000000b7527c423df68abb627d67a0666fdcee; successCount=1|Fri, 14 Jul 2017 15:38:07 GMT',
        # 'Host': 'doubanbook.sogou.com',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    session = Session()
    queue = RedisQueue()
    # mysql = MySQL()
    row = 1
    col = 0

    saver = Saver()

    def __init__(self, keyword):
        self.keyword = keyword

    def start(self):
        """
        初始化工作
        """
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '/?' + urlencode({'key': self.keyword})
        doubanbook_request = DangdangRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        self.queue.add(doubanbook_request)
    
    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """

        soup = BeautifulSoup(response.text, 'lxml')

        for book in soup.find_all(dd_name="单品标题"):
            url = book.get('href')
            dangdang_request = DangdangRequest(url=url, callback=self.parse_detail)
            yield dangdang_request

        next = soup.find(title="下一页").get("href")
        print(next)

        if next and int(next[-1]) < 2:
            url = self.base_url + next
            dangdang_request = DangdangRequest(url=url, callback=self.parse_index)
            yield dangdang_request

    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 书籍信息
        """
        soup = BeautifulSoup(response.text, 'lxml')

        try:
            title = soup.find('h1').get_text()
            title = title.strip()
        except Exception as e:
            print(e)
            title = ''

        try:
            descrip = soup.find('span', class_="head_title_name").get_text()
            descrip = descrip.strip()
        except Exception as e:
            print(e)
            descrip = ''

        try:
            author = soup.find_all('span', class_="t1", limit=3)[0].get_text()
            author = author.strip()
        except Exception as e:
            print(e)
            author = ''

        try:
            publisher = soup.find_all('span', class_="t1", limit=3)[1].get_text()
            publisher = publisher.strip()
        except Exception as e:
            print(e)
            publisher = ''

        try:
            pubdate = soup.find_all('span', class_="t1", limit=3)[2].get_text()
            pubdate = pubdate.strip()
        except Exception as e:
            print(e)
            pubdate = ''

        try:
            nowprice = soup.find(id="dd-price").get_text()
            nowprice = nowprice.strip()
        except Exception as e:
            print(e)
            nowprice = ''

        try:
            oriprice = soup.find(id="original-price").get_text()
            oriprice = oriprice.strip()
        except Exception as e:
            print(e)
            oriprice = ''

        try:
            elebookprice = soup.find(id="e-book-price").get_text()
            elebookprice = elebookprice.strip()
        except Exception as e:
            print(e)
            elebookprice = ''

        data = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'pubdate': pubdate,
            'nowprice': nowprice,
            'oriprice': oriprice,
            'elebookprice': elebookprice,
            'descrip': descrip,
        }
        yield data
    
    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return: 响应
        """
        try:
            return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout, allow_redirects=False)
        except (ConnectionError, ReadTimeout) as e:
            print(e.args)
            return False
    
    def error(self, doubanbook_request):
        """
        错误处理
        :param weixin_request: 请求
        :return:
        """
        doubanbook_request.fail_time = doubanbook_request.fail_time + 1
        print('Request Failed', doubanbook_request.fail_time, 'Times', doubanbook_request.url)
        if doubanbook_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(doubanbook_request)


    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            doubanbook_request = self.queue.pop()
            callback = doubanbook_request.callback
            print('Schedule', doubanbook_request.url)
            response = self.request(doubanbook_request)
            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                if results:
                    for result in results:
                        print('New Result', type(result))
                        if isinstance(result, DangdangRequest):
                            self.queue.add(result)
                        if isinstance(result, dict):
                            print(result)
                            self.saver.save(result, self.row, self.col)
                            self.row += 1
                            print(self.row)
                else:
                    self.error(doubanbook_request)
            else:
                self.error(doubanbook_request)
    
    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    keyword = "大数据"
    spider = Spider(keyword)
    spider.run()
    spider.saver.workbook.close()