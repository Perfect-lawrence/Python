#!/usr/bin/env python3

import pymysql
#conn = pymysql.connect(host='192.168.5.6',password='12345678',port=3388,user='lawrence',charset='utf8')
# # 打开数据库连接
conn = pymysql.connect(host='192.168.5.6',port=3388,user='lawrence',password='12345678',charset='utf8')
# 使用cursor()方法获取操作游标
cursor = conn.cursor()

sql = "select version()"
try:
    #  执行SQL语句
    cursor.execute(sql)
    version = cursor.fetchall()
    print(version)
except:
    print("链接失败")

conn.close()
