from django.db import models
from datetime import datetime
from django.utils import timezone
from random import *


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    add = models.TextField(default='')
    Email = models.EmailField(default='',help_text='enter your email :')
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=8)
    confirm_password=models.CharField(max_length=8)
    date=models.DateField(default=datetime.now())
    Time=models.TimeField(default=datetime.now())
    birth_date=models.DateField(default=timezone.now)
    photo=models.FileField()
