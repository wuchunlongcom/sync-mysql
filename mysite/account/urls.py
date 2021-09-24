from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'list/mysql/$', views.list_db, name='list_db'),    
    url(r'sync_db/$', views.sync_db, name='sync_db'),  # 不用定时任务-更新数据库
    url(r'crontab/$', views.crontab, name='crontab'),  # 定时任务-更新数据库   
        
    url(r'', views.list_mysql, name='list_mysql'),   #必须放在最后
]
