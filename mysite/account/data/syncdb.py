#!/usr/bin/env python

import os
import django
import datetime
import xlrd
from account.models import Student

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

def syncdb():
    items = getData('select * from account_student')
    items = [Student(sid=i[1], name=i[2], address=i[3]) for i in items]
    Student.objects.bulk_create(items, batch_size=20)
    return '%s' %len(items)



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
    syncdb()
