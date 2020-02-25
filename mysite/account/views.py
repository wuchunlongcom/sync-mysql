# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from .models import Student
from account.data.syncdb import getData
from django.contrib.auth.decorators import login_required
from mysite.settings import BASE_DIR    
    
def list_mysql(request):
    meg = 'ok'
    
    data_list = getData('select * from account_student')
    print(type(data_list[0]), data_list[0:10])

    return render(request, 'account/list_mysql.html', context=locals()) 

def list_db(request):
    data_list = Student.objects.all()
    return render(request, 'account/list_db.html', context=locals()) 


@login_required
def syncdb(request):
    '''
    1. 文件不存在：显示"同步数据库"按钮，点击按钮，创建一个文件
    2. 文件存在：显示"数据库同步中，请稍等..."文本
    '''
    if not request.user.is_superuser:
        return HttpResponseRedirect('/')

    STATEFILE = os.path.join(BASE_DIR, 'account','data', 'statefile.txt') # 状态文件
    meg = '更新数据库'
    if request.method == 'POST' and not os.path.exists(STATEFILE):
        with open(STATEFILE, 'w+') as fp:
            fp.write('0')
            
        data_list = getData('select * from account_student')
        for d in data_list:
            s = Student() 
            s.sid = d[1]   # id d[0]
            s.name = d[2]
            s.address = d[3]
            s.save() 
        meg = '数据库%s条记录更新完毕！'%(len(data_list))
                                   
    if os.path.isfile(STATEFILE): #判断文件
        os.remove(STATEFILE)       

    syncingdb = os.path.exists(STATEFILE)
    return render(request, 'account/syncdb.html', context=locals())
