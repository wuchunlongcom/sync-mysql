#!/usr/bin/env python

import os
import django
import datetime
import xlrd

def getData(sql):
    import pymysql
    db = pymysql.Connect(host="127.0.0.1",
                         user="root",
                         password="12345678",
                         port=3306,
                         db="studb",
                         charset="utf8")
    
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    ret = [[j or '' for j in i] for i in result]
    cur.close
    db.close()
    return ret    

""" Oracle
def getData(sql):
    import cx_Oracle
    db = cx_Oracle.connect("jw_user", "Hdlgdx18", "172.20.8.37:1521/orcl", encoding="UTF-8")
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    ret = [[j or '' for j in i] for i in result]
    cur.close
    db.close()
    return ret

"""

if __name__ == "__main__":
    getData('select * from account_student')
