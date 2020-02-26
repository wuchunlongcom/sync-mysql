from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'list/mysql/$', views.list_db, name='list_db'),    
    url(r'sync_db/$', views.sync_db, name='sync_db'),
    url(r'crontab/$', views.crontab, name='crontab'),     
        
    url(r'', views.list_mysql, name='list_mysql'),   #必须放在最后
]
