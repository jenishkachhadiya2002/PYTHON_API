from django.contrib import admin
from django.urls import path,include
from.views import *

urlpatterns = [
     path('',gett),
    path('post/',postt),
    path('put/<id>/',putt),
    path('patch/<id>/',patchh),
    path('delete/<id>/',deletee)
]




          