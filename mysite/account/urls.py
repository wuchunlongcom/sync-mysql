from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'list/mysql/$', views.list_db, name='list_db'),    
    url(r'syncdb/$', views.syncdb, name='syncdb'),   
        
    url(r'', views.list_mysql, name='list_mysql'),   #必须放在最后
]
