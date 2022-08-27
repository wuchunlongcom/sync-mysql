# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from .models import Student
from account.data.syncdb import getData, syncdb
from django.contrib.auth.decorators import login_required
from mysite.settings import STATEFILE    

def list_mysql(request):
    meg = 'ok'
    global STATEFILE    
    # 空跑 定时执行任务
    if os.path.isfile(STATEFILE): #判断文件
        os.remove(STATEFILE) 
    
    data_list = getData('select * from account_student')
    return render(request, 'account/list_mysql.html', context=locals()) 

def list_db(request):
    global STATEFILE    
    # 空跑 定时执行任务
    if os.path.isfile(STATEFILE): #判断文件
        os.remove(STATEFILE) 
    
    data_list = Student.objects.all()    
    return render(request, 'account/list_db.html', context=locals()) 


@login_required
def sync_db(request):
    '''
    不用定时任务(删除状态文件，定时执行任务空跑)   
    空跑 定时执行任务
    1. 状态文件不存在： 定时执行任务空跑
    2. 文件存在：显示"数据库同步中，请稍等..."文本
    '''
    meg = '更新数据库'

    global STATEFILE    
    # 删除状态文件，定时执行任务空跑
    if os.path.isfile(STATEFILE): #判断文件
        os.remove(STATEFILE) 
             
    if request.method == 'POST' :
        meg = syncdb()
        meg = '数据库%s条记录更新完毕！' %meg if 'err' not in meg else meg            
                                               
    syncingdb = os.path.isfile(STATEFILE)
    return render(request, 'account/sync_db.html', context=locals())

@login_required
def crontab(request):
    ''' 
    状态文件写'0',使用定时执行任务   
    1. 调用该视图，状态文件文件如果不存在：显示"同步数据库"按钮,点击"同步数据库"按钮，创建一个状态文件,显示"数据库同步中，请稍等..."文本；
    2. 定时器每分钟执行一次，执行更新数据库数据任务，任务完成删除状态文件文件；
   
    '''     
    global STATEFILE
    #if os.path.isfile(STATEFILE): #判断文件
    #    os.remove(STATEFILE) 
    
    # 状态文件写'0',使用定时执行任务
    if request.method == 'POST':
        with open(STATEFILE, 'w+') as fp:
            fp.write('0')
    
    syncingdb = os.path.isfile(STATEFILE)    
    return render(request, 'account/crontab.html', context=locals())

    