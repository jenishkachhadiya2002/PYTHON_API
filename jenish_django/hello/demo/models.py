from django.db import models
from datetime import datetime
from django.utils import timezone
from django_countries.fields import CountryField

GENDER_CHOICES = [
        ( 'Male','Male'),
        ( 'Female','Female'),
        ('Other','Other'),
    ]
STATE_CHOICES=[
                ('Andhra Pradesh','Andhra Pradesh'),
                ('Arunachal Pradesh','Arunachal Pradesh'),
                ('Assam', 'Assam'),
                ('Bihar','Bihar'),
                ('Chhattisghar','Chhattisgarh'),
                ('Delhi','Delhi'),
                ('Goa','Goa'),
                ('Gujarat','Gujarat'), 
                ('Haryana','Haryana'), 
                ('Himachal Pradesh','Himachal Pradesh'), 
                ('Jharkhand','Jharkhand'),
                ('Karnataka','Karnataka'),
                ('Kerala','Kerala'), 
                ('Madhya Pradesh','Madhya Pradesh'),
                ('Maharashtra','Maharashtra'), 
                ('Manipur','Manipur'),
                ('Meghalaya','Meghalaya'),
                ('Mizoram','Mizoram'),
                ('Nagaland','Nagaland'),
                ('Odisha','Odisha'),
                ('Punjab','Punjab'),
                ('Rajasthan','Rajasthan'),
                ('Sikkim','Sikkim'),
                ('Tamil Nadu','Tamil Nadu'),
                ('Telangana','Telangana'),
                ('Tripura','Tripura'), 
                ('Uttar Pradesh','Uttar Pradesh'),
]
CITY_CHOICE=[

        ('AHMADABAD','AHMADABAD')
        ,('AMARELI','AMRELI')
        ,('ANAND','ANAND')
        ,('BANASKATHA','BANSKATHA')
        ,('BHARUCH','BHARUCH')
        ,('BHAVNAGAR','BHAVNAGAR')
        ,('DAHOD','DAHOD')
        ,('DANG','DANG')
        ,('GANDINAGAR','GANDHINAGAR')
        ,('JAMNAGAR','JAMNAGAR')
        ,('JUNAGADH','JUNAGADH')
        ,('KACHHBHUJ','KACHCHHBHUJ')
        ,('KHEDA','KHEDA')
        ,('MAHESANA','MAHESANA')
        ,('NARMADA','NARMADA')
        ,('NAVSARI','NAVSARI')
        ,('PANCHMAHAL','PANCHMAHAL')
        ,('PATAN','PATAN')
        ,('PORBANDAR','PORBANDAR')
        ,('RAJKOT','RAJKOT')
        ,('SABARKATHA','SABARKATHA')
        ,('SURAT','SURAT')
        ,('SURENDRAGAR','SURENDRANAGR')
        ,('TAPI','TAPI')
        ,('VADODRA','VADODRA')
        ,('VALSAD','VALSAD'),
] 
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField(default=18)
    Address = models.TextField(default='')
    Email = models.EmailField(default='',help_text='enter your email :')
    Mobile=models.CharField(max_length=10)
    Password=models.CharField(max_length=8)
    Confirm_Password=models.CharField(max_length=8)
    Date=models.DateTimeField(default=timezone.now)
    Time=models.TimeField(default=timezone.now)
    Birth_Date=models.DateField(default=datetime.now)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    Country=CountryField(null=True)
    State=models.CharField(max_length=17,choices=STATE_CHOICES,blank=True)
    City=models.CharField(max_length=11,choices=CITY_CHOICE,blank=True)
   
    
  