# encoding=utf-8

import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'




# 查询数据库，并返回数据
def query_sql(v_sql):
    conn = cx_Oracle.connect('APP_TOMS/APP_TOMS@122.224.168.146:65521/orcl')  # 连接数据库
    c = conn.cursor()  # 获取cursor
    try:
        # 解析sql语句
        c.parse(v_sql)
    # 捕获SQL异常
    except cx_Oracle.DatabaseError as e:
        print(e)
    c.execute(v_sql)  # 使用cursor进行各种操作
    row = c.fetchone()  # 可以调用cursor.fetchall()一次取完所有结果，或者cursor.fetchone()一次取一行结果
    c.close()  # 关闭cursor
    conn.close()  # 关闭连接

    return row


# 访问数据库，插入数据
def insert_sql(v_sql, data):
    conn = cx_Oracle.connect('APP_TOMS/APP_TOMS@122.224.168.146:65521/orcl')
    c = conn.cursor()
    try:
        c.parse(v_sql)
    except cx_Oracle.DatabaseError as e:
        print(e)
    c.execute(v_sql, data)
    conn.commit()
    c.close()
    conn.close()


def delete_sql(v_sql):
    conn = cx_Oracle.connect('APP_TOMS/APP_TOMS@122.224.168.146:65521/orcl')
    c = conn.cursor()
    try:
        c.parse(v_sql)
    except cx_Oracle.DatabaseError as e:
        print(e)
    c.execute(v_sql)
    conn.commit()
    c.close()
    conn.close()

# sql="select * from T_BICYCLE"
# q=query_sql(sql)
# print(q)
# for each in q:
#     isinstance(q,list)
#     print(each)



