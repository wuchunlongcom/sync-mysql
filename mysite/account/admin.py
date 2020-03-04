"""
### admin 添加一个按钮注意事项 
      
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
from account.data.syncdb import syncdb

STATEFILE = os.path.join(settings.BASE_DIR, 'account','data', 'statefile.txt') # 状态文件

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
        2、按‘数据库状态’按钮，判断statefile.txt 状态文件是否存在
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

    change_list_template = 'entities/heroes_button.html'
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(r'^upload_db/$',
                self.admin_site.admin_view(self.upload_db),
                name='photologue_upload_db'),  
        ]
        return custom_urls + urls

    def upload_db(self, request):
        
        context = {
            'title': ('Upload db'),
            'app_label': self.model._meta.app_label,
            'opts': self.model._meta,
            'has_change_permission': self.has_change_permission(request)
        }

        if request.method == 'POST':                      
            
            if not os.path.isfile(STATEFILE):
       
                with open(STATEFILE,'w+') as f:
                    f.write('1111')  # '0'禁用，不使用定时执行任务。
                
                meg = syncdb()
                meg = '%s 条记录更新完成.' %meg if 'err' not in meg else meg
                             
                if os.path.isfile(STATEFILE): 
                    os.remove(STATEFILE) 
                    
            self.message_user(request, meg)
                             
            return HttpResponseRedirect("../")
            
        else: 
                   
            isfile = True if os.path.isfile(STATEFILE) else False
            context.update({'isfile':isfile, 'meg':'再次确认是否更新？',})
            
        return render(request, 'entities/upload_db.html', context)
