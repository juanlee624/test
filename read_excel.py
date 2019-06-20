# encoding=utf-8

import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import xlrd
from xlutils.copy import copy
from connoracle import query_sql, insert_sql

# fname = 'F:\\work\\总局项目\\20190426\\(模拟板)2018年度全国税务稽查统计报表（年报）.xls'  # Windows系统下的目录必须使用两个\
fname='F:\学习\practice\T_BICYCLE.xlsx'
# 打开文件
filename = xlrd.open_workbook(fname)
names=filename.sheet_names() #获取文件中所有表单的名字
print(names)#打印所有表单的名字
sheets=filename.nsheets # 获取当前文档的表(得到的是sheet的个数，一个整数）
sheet = filename.sheets()[0]#获取第一个表单的内容


name = sheet.cell_value(1, 0)  # 获取表单第二行第一列的数据
lat = sheet.cell_value(1, 1)  # 获取表单第二行第二列的数据
lng = sheet.cell_value(1, 2)  # 获取表单第二行第三列的数据
capacity = sheet.cell_value(1, 3)  # 获取表单第二行第四列的数据
availbike = sheet.cell_value(1, 4)  # 获取表单第二行第五列的数据
address = sheet.cell_value(1, 5)  # 获取表单第三行第六列的数据

sql = "insert into T_BICYCLE(ID,NAME,LAT,LNG,CAPACITY,AVAILBIKE,ADDRESS,CREATETIME) values(:0, :1,:2,:3,:4,:5,systimestamp)"
print(sql)
data = [name,lat,lng,capacity,availbike,address]
print(data)
insert_sql(sql, data)

# 获取行数
nrows = sheet.nrows
# 获取列数
ncols = sheet.ncols

# ---------------------
# 作者：磨刀大神
# 来源：CSDN
# 原文：https: // blog.csdn.net / weixin_43241054 / article / details / 89642648
# 版权声明：本文为博主原创文章，转载请附上博文链接！