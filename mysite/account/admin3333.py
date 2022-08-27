"""
### admin3333 没有作用，作为资料保存！
      
```
1、添加admin模板    ../templates/admin/account/photo/upload_zip.html；
2、路由^upload_zip/名称与函数名称一致；
3、路由映射名称 name='photologue_upload_zip')  在admin模板中使用；
4、context的使用。

"""
import os
from django.shortcuts import render
from django.conf.urls import url
from django.contrib import admin
from .models import Student
from account.data.syncdb import getData
from django.conf import settings
from django.http.response import HttpResponseRedirect, HttpResponse

STATEFILE = os.path.join(settings.BASE_DIR, 'account','data', 'syncdbstatus.txt') # 状态文件

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'sid', 'name','address',)
    
    """ admin 添加按钮
        一、关于访问后台admin数据库问题：
        1、在此写入代码后，首次访问页面时，是执行后台代码的，以后再访问该页面，就不执行后台代码了。
        访问页面 http://localhost:8000/admin/classroom/course/
        2、添加按钮，后台数据如何传到前端？
        
        二、本例采用另外方法，实现下列功能：
        1、admin 添加按钮
        2、按‘数据库状态’按钮，判断syncdbstatus.txt 状态文件是否存在
        如果状态文件不存在(允许更新同步)，显示‘数据库状态’按钮、‘同步数据库’按钮。按‘同步数据库’按钮，创建一个状态文件
        如果状态文件存在(正在同步中)，显示‘数据库状态’按钮、‘数据库同步中，请稍等...’。 
        
        三、admin 后台实现更新数据库数据
        1、 用命令不能更新数据(本机运行正常，部署后不能更新数据)，原因不清楚？
        2、本实例用函数实现， admin后台实现更新数据库数据，成功！
        3、更新数据库数据的逻辑：
        （1）创建状态文件
        （2）更新数据库数据
        （3）删除状态文件
          
    """
    
    change_list_template = "entities/sync-in-progress.html"     
    def get_urls(self):        
        urls = super().get_urls()
        my_urls = [
            url('sync_in_progress/', self.sync_in_progress),
            url('allow_sync/', self.allow_sync),
        ]
        return my_urls + urls
    
    def sync_in_progress(self, request):
        """ 同步数据库(正在同步中) """
        if request.method == 'POST':

            with open(STATEFILE,'w+') as fp:  
                fp.write('0') 
                                            
            data_list = getData('select * from account_student')
            for d in data_list:
                s = Student() 
                s.sid = d[1]   # id d[0]
                s.name = d[2]
                s.address = d[3]
                s.save() 
                
                   
            if os.path.isfile(STATEFILE): #判断文件
                os.remove(STATEFILE)                                         
            self.message_user(request, '%s 条记录同步完成.' %len(data_list)) 
            self.change_list_template = "entities/allow-sync.html"             
        return HttpResponseRedirect("../")
     
    def allow_sync(self, request):
        """判断文件是否存在"""        
        if os.path.exists(STATEFILE):
            # 状态文件存在,显示‘数据库状态’按钮,  正在同步... 此时是不能更新数据库数据
            self.change_list_template = "entities/sync-in-progress.html"             
        else:
            # 状态文件不存在,显示‘数据库状态’按钮, '更新数据库'    允许更新数据库数据
            self.change_list_template = "entities/allow-sync.html" 
        return HttpResponseRedirect("../")



