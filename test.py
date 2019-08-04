# -*- coding: utf-8 -*-

'''
@Author : siran
@time : 2019/7/28 14:54
@File : test.py
@Software : PyCharm
'''


import requests
from lxml import etree
from selenium import webdriver
import time

url = 'https://book.douban.com/subject_search?search_text=大数据&start=15'
url1 = 'https://read.douban.com/search?q=%E5%A4%A7%E6%95%B0%E6%8D%AE'
url2 = 'http://search.dangdang.com/?key=%B4%F3%CA%FD%BE%DD&act=input'
url3 = 'http://product.dangdang.com/22928335.html'

# res = requests.get('https://book.douban.com/subject_search?search_text=大数据&start=15')

# print(res.text)

browers = webdriver.PhantomJS(executable_path=r'E:\Program Files (x86)\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# 设置窗口大小
# browers.set_window_size(1366, 768)
# # 页面的加载超时时间
# browers.set_page_load_timeout(10)
# # script脚本的超时时间
# browers.set_script_timeout(10)
#
browers.get(url3)
#
# time.sleep(2)

# su = browers.find_element_by_xpath('//*[@class="sc-bZQynM iYyDDv sc-bxivhb hRIaFd"]')
# su = browers.find_element_by_class_name('works-item ')
# print(su)

htmls = browers.page_source
#
print(htmls)
html = etree.HTML(htmls)
info = html.xpath('//div[contains(@class,"sale_box clearfix")/div/div/h1')
print(info)

# #
# # print(html)
# books = html.xpath('//div[contains(@class,"section-works")]//li[contains(@class,"works-item ")]')
#
# for book in books:
#     b = book.xpath('./div')
#     print(b)
# print(len(books))
# # # books = html.xpath('//div[contains(@class,"root")]//div[@class="detail"]')
# print(books)



