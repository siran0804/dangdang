# -*- coding: utf-8 -*-

'''
@Author : siran
@time : 2019/8/3 23:30
@File : savetoexcel.py
@Software : PyCharm
'''

import xlsxwriter

class Saver(object):

    def __init__(self):
        workbook = self.workbook = xlsxwriter.Workbook('./result.xlsx')
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


