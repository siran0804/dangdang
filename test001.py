# -*- coding: utf-8 -*-

'''
@Author : siran
@time : 2019/8/1 10:27
@File : test001.py.py
@Software : PyCharm
'''

import requests
from lxml import etree
from bs4 import BeautifulSoup
# from selenium import webdriver

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

res = requests.get('http://product.dangdang.com/24189095.html', headers = headers  )
res1 = requests.get('http://search.dangdang.com/?key=大数据')

soup = BeautifulSoup(res1.text, 'lxml')

all_book = soup.find_all(dd_name="单品标题")
print(len(all_book))
for book in all_book:
    print(book.get('href'))
# print(all_book)
# print(all_book)
# link_list = all_book.find_all('a')
# print(link_list)

link = soup.find(title="下一页")
print(type(link.get('href')))

# for link in soup.find_all(title="下一页"):
#     print(link)
#     print(link.get('href'))



# print(res.text)
soup = BeautifulSoup(res.text, 'lxml')
soup.find_all('h1')

for ele in soup.find_all('h1'):
    print(ele.get_text())

for ele in soup.find_all('span', class_="head_title_name"):
    print(ele.get_text())

for ele in soup.find_all('span', class_="t1", limit=3):
    test = ele.get_text()
    print(type(test))
    l = test.split(':')
    print(l)

for ele in soup.find_all(id="dd-price"):
    print(ele.get_text())
    # print(ele.get_text())

for ele in soup.find_all(id="original-price"):
    print(ele.get_text())

for ele in soup.find_all(id="e-book-price"):
    print(ele.get_text())
    # print(ele.get_text())





