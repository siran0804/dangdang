# -*- coding: utf-8 -*-

'''
@Author : siran
@time : 2019/8/3 23:30
@File : request.py
@Software : PyCharm
'''

from dangdangbook.config import *
from requests import Request


class DangdangRequest(Request):
    def __init__(self, url, callback, method='GET', headers=None, need_proxy=False, fail_time=0, timeout=TIMEOUT):
        Request.__init__(self, method, url, headers)
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout
