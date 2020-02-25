# -*- coding: UTF-8 -*-
import os
import sys
import django
import random

print('python 版本: %s。\ndjango版本: %s。'%(sys.version, django.get_version()))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings_mysql")
    django.setup()
   
    from account.models import Student
    import random    

    
    """
    插入测试数据
    """
    Student().delete  
    for i in range(0, 1000):
        studentNum = int(random.uniform(0, 1) * 10000000000)
        student = Student()
        student.sid = str(studentNum)
        student.name = 'name-%s' %i
        student.address = 'address-%s' %i
        student.save()
        
    print('mysql init ok!')