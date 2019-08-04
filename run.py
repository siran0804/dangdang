# -*- coding: utf-8 -*-

'''
@Author : siran
@time : 2019/8/3 23:30
@File : run.py
@Software : PyCharm
'''

from dangdangbook.spider import Spider

if __name__ == '__main__':
    keyword = "物联网"
    spider = Spider(keyword)
    spider.run()
