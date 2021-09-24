# -*- coding: UTF-8 -*-
import os
import sys
import django
import random

print('python 版本: %s。\ndjango版本: %s。'%(sys.version, django.get_version()))

if __name__ == "__main__":
    # 数据模型与mysql关联 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings_mysql")
    django.setup()
   
    from account.models import Student
    import random    
    
    # 给mysql account_student表，初始化数据【50 0000 测试通过】
    [i.delete() for i in Student.objects.all()] # 删除数据库记录
    items = [Student(sid='sid-%s' %i, name='name-%s' %i, 
                     address='address-%s' %i) for i in range(0, 10000)]  
    Student.objects.bulk_create(items, batch_size=20)
   