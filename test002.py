# -*- coding: utf-8 -*-

'''
@Author : siran
@time : 2019/8/3 23:48
@File : test002.py
@Software : PyCharm
'''

import xlsxwriter

class Saver(object):

    def __init__(self):
        workbook = self.workbook = xlsxwriter.Workbook('./test.xlsx')
        self.worksheet = workbook.add_worksheet()
        bold_format = workbook.add_format({'bold': True})
        self.worksheet.write('A1', 'title', bold_format)
        self.worksheet.write('B1', 'author', bold_format)
        self.worksheet.write('C1', 'publisher', bold_format)
        self.worksheet.write('D1', 'pubdate', bold_format)
        self.worksheet.write('E1', 'nowprice', bold_format)
        self.worksheet.write('F1', 'oriprice', bold_format)
        self.worksheet.write('G1', 'elebookprice', bold_format)
        self.worksheet.write('H1', 'descrip', bold_format)


    def save(self, data, row, col):
        self.worksheet.write_string(row, col, data['title'])
        self.worksheet.write_string(row, col + 1, data['author'])
        self.worksheet.write_string(row, col + 2, data['publisher'])
        self.worksheet.write_string(row, col + 3, data['pubdate'])
        self.worksheet.write_string(row, col + 4, data['nowprice'])
        self.worksheet.write_string(row, col + 5, data['oriprice'])
        self.worksheet.write_string(row, col + 6, data['elebookprice'])
        self.worksheet.write_string(row, col + 7, data['descrip'])
        row += 1



if __name__ == '__main__':
    saver = Saver()
    row = 1
    col = 0
    data = {'title': '大数据高可用环境搭建与运维', 'author': '作者:天津滨海迅腾科技集团有限公司 编', 'publisher': '出版社:天津大学出版社', 'pubdate': '出版时间:2019年03月', 'nowprice': '¥33.80', 'oriprice': '¥49.00', 'elebookprice': '', 'descrip': ''}
    saver.save(data, row, col)
    saver.workbook.close()