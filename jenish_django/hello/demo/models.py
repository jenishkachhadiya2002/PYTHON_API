from django.db import models
from datetime import datetime
from django.utils import timezone
from django_countries.fields import CountryField

GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
STATE_CHOICES=[('A','Andhra Pradesh'),
               ('A','Arunachal Pradesh'),
               ('A', 'Assam'),
               ('B','Bihar'),
               ('C','Chhattisgarh'),
               ('D','Delhi'),
                ('G','Goa'),
                ('G','Gujarat'), 
                ('H','Haryana'), 
                ('H','Himachal Pradesh'), 
                ('J','Jharkhand'),
                ('K','Karnataka'),
                ('K','Kerala'), 
                ('M','Madhya Pradesh'),
                ('M','Maharashtra'), 
                ('M','Manipur'),
                ('M','Meghalaya'),
                ('M','Mizoram'),
                ('M','Nagaland'),
                ('O','Odisha'),
                ('P','Punjab'),
                ('R','Rajasthan'),
                ('S','Sikkim'),
                ('T','1Tamil Nadu'),
                ('T','Telangana'),
                ('T','Tripura'), 
                ('U','Uttar Pradesh'),
]

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
    photo=models.ImageField()
    country=CountryField()
    state=models.CharField(max_length=1,choices=STATE_CHOICES,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
  
