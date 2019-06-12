# encoding=utf-8

import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import xlrd
from xlutils.copy import copy
from connoracle import query_sql, insert_sql

# fname = 'F:\\work\\总局项目\\20190426\\(模拟板)2018年度全国税务稽查统计报表（年报）.xls'  # Windows系统下的目录必须使用两个\
fname='E:\study\python\data.xls'
# 打开文件
filename = xlrd.open_workbook(fname)
# 获取当前文档的表(得到的是sheet的个数，一个整数）
# sheets=filename.nsheets
# 获取Excel中第四个sheet页
# sheet = filename.sheets()[3]
sheet = filename.sheets()

ts_hc = sheet.cell_value(6, 2)  # 偷税户次
ts_cbsk = sheet.cell_value(6, 3)  # 偷税查补税款
ts_znj = sheet.cell_value(6, 4)  # 偷税滞纳金
ts_wfsd = sheet.cell_value(6, 5)  # 偷税没收违法所得
ts_fk = sheet.cell_value(6, 6)  # 偷税罚款
ts_cbze = sheet.cell_value(6, 7)  # 偷税查补总额

jg = sheet.cell_value(2, 0)  # 报送机关
jg = jg[5:]
sql = "insert into MX_JCCGJK_SWJCCGB(SWJGMC,JCLASL,JCRKJE,SJCLSJ) values(:1, :2,:3,systimestamp)"

data = [jg, ts_hc, ts_cbze]
print(data)
insert_sql(sql, data)

# 获取行数
nrows = sheet.nrows
# 获取列数
ncols = sheet.ncols
print(jg)

# ---------------------
# 作者：磨刀大神
# 来源：CSDN
# 原文：https: // blog.csdn.net / weixin_43241054 / article / details / 89642648
# 版权声明：本文为博主原创文章，转载请附上博文链接！