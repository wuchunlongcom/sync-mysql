
from django.db import models
    
class Student(models.Model):
    sid = models.CharField(verbose_name='sid',  max_length=20, blank=True)
    name = models.CharField(verbose_name='姓名',  max_length=20, blank=True)
    address = models.CharField(verbose_name='地址',  max_length=50, blank=True)

    def __str__(self):
        return self.name