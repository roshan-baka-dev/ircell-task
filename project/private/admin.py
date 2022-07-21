from django.contrib import admin
# from numpy import 

#written separately to store data so that admin can see
from private.models import student
# Register your models here.

admin.site.register(student)

