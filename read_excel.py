# encoding=utf-8

import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import xlrd
from xlutils.copy import copy
from connoracle import query_sql, insert_sql

fname='F:\学习\practice\T_BICYCLE.xlsx'#excel附件位置
filename = xlrd.open_workbook(fname)# 打开文件
names=filename.sheet_names() #获取文件中所有表单的名字
print(names)#打印所有表单的名字
sheets=filename.nsheets # 获取当前文档的表(得到的是sheet的个数，一个整数）
sheet = filename.sheets()[0]#获取第一个表单的内容
nrows = sheet.nrows
print('表单的行数：%d'%nrows) #获取查询表单的行数
ncols = sheet.ncols # 获取查询表单的列数
print('表单的列数：%d'%ncols)

for i in range(1,nrows):
     sql = "insert into T_BICYCLE(NAME,LAT,LNG,CAPACITY,AVAILBIKE,ADDRESS,CREATETIME) values(:0,:1,:2,:3,:4,:5,systimestamp)"
     print(sql)
     data = sheet.row_values(i, start_colx=0, end_colx=ncols - 1)
     print(data)
     insert_sql(sql, data)

