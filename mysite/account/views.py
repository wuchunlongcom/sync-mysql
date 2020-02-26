# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from .models import Student
from account.data.syncdb import getData, syncdb
from django.contrib.auth.decorators import login_required
from mysite.settings import BASE_DIR    
    
def list_mysql(request):
    meg = 'ok'
    
    data_list = getData('select * from account_student')
    #print(type(data_list[0]), data_list[0:10])

    return render(request, 'account/list_mysql.html', context=locals()) 

def list_db(request):
    data_list = Student.objects.all()
    return render(request, 'account/list_db.html', context=locals()) 


@login_required
def sync_db(request):
    '''
    1、'0'禁用，不使用定时执行任务
    2. 文件不存在：显示"同步数据库"按钮，点击按钮，创建一个文件
    3. 文件存在：显示"数据库同步中，请稍等..."文本
    '''
    if not request.user.is_superuser:
        return HttpResponseRedirect('/')

    STATEFILE = os.path.join(BASE_DIR, 'account','data', 'statefile.txt') # 状态文件
    meg = '更新数据库'
    if request.method == 'POST' and not os.path.exists(STATEFILE):
        with open(STATEFILE, 'w+') as fp:
            fp.write('11')  # '0'禁用，不使用定时执行任务。
            
        meg = syncdb()
        meg = '数据库%s条记录更新完毕！' %meg if 'err' not in meg else meg            
                                               
    if os.path.isfile(STATEFILE): #判断文件
        os.remove(STATEFILE)       

    syncingdb = os.path.exists(STATEFILE)
    return render(request, 'account/sync_db.html', context=locals())

@login_required
def crontab(request):
    ''' 
    状态文件写'0',使用定时执行任务   
    1. 调用该视图，状态文件文件不存在：显示"同步数据库"按钮,点击"同步数据库"按钮，创建一个状态文件,显示"数据库同步中，请稍等..."文本；
    2. 定时器每分钟执行一次，执行更新数据库数据任务，任务完成删除状态文件文件；
    3. 再次调用该视图，执行1步骤
    '''
    if not request.user.is_superuser:
        return HttpResponseRedirect('/')

    STATEFILE = os.path.join(BASE_DIR, 'account','data', 'statefile.txt') # 状态文件

    if request.method == 'POST' and not os.path.exists(STATEFILE):
        with open(STATEFILE, 'w+') as fp:
            fp.write('0')

    syncingdb = os.path.exists(STATEFILE)
    return render(request, 'account/crontab.html', context=locals())

    