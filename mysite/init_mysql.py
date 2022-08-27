# -*- coding: UTF-8 -*-
import os
import sys
import django
import random

if __name__ == "__main__":
    # 数据模型与mysql关联 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings_mysql")
    django.setup()
   
    from account.models import Student
    import random    
    init_num = 1000  # 初始化1000条记录
    # 给mysql account_student表，初始化数据【50 0000 测试通过】
    [i.delete() for i in Student.objects.all()] # 删除数据库记录
    items = [Student(sid='sid-%s' %i, name='name-%s' %i, 
                     address='address-%s' %i) for i in range(0, init_num)]  
    Student.objects.bulk_create(items, batch_size=20)
    print('完成mysql初始化%s条记录.'%(init_num))