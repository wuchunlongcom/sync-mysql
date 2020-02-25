# -*- coding: utf-8 -*-

"""
单元(类、函数)测试方法：Eclipse环境 选择运行图标 --> Run As --> Python Run 
pageAPI.py  分页类
wcl6005@126.com    2017.2.5
"""

PAGE_NUM = 2 # 设置每页显示数
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def djangoPage(contact_list, page, num):
    """
    使用该函数步骤：
    一、拷入文件： ./templates/page/djangopage.html
    二、views.py
    1、引用： from myAPI.pageAPI import djangoPage
    2、设置每页显示数：PAGE_NUM = 20 #每页显示数
    3、方法：def show(request):  -->   def show(request, page):
    4、在返回html前台以前加入下列两条语句，其中data_list数据库记录或列表，需要注意的data_list是前后的是不一样的。
      data_list, pageList, num_pages, page = djangoPage(data_list, page, PAGE_NUM) #调用分页函数
      offset = PAGE_NUM * (page - 1)
    三、更改路由：r'^show/'  -->   r'^show/(?P<page>\d*)?$'
    四、在html前台文件中加入分布：<div style="padding-left:520px;"">{% include 'page/djangopage.html' %}  </div> <!--分页--> 

    适用django分页  1、data_list数据库记录或列表；2、page当前页；3、设置每页显示数 num
     
    综合应用实例：http://localhost:8888/control/index/ 。   有道云笔记： 分页 page   
    """
    paginator = Paginator(contact_list, num) 
    try:
        page = int(page)
    except Exception as _e:
        page = 1
 
    try:
        model_list = paginator.page(page)
    except PageNotAnInteger:
        model_list = paginator.page(1)
    except EmptyPage:
        model_list = paginator.page(paginator.num_pages)
         
    pageList = list(paginator.page_range)
    if page < (paginator.num_pages)-3:
        pageList[page+2:-1] = ['...']
    if page > 1+3:
        pageList[1:page-3] = ['...']        
    return model_list,pageList,paginator.num_pages,page

