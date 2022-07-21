import email
from pyexpat import model
from django.db import models

# Create your models here.
#pasted from django db class documentation

from django.db import models

#to store data we need class in models
#models are a piece of information

class student(models.Model):
    name = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    roll = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

#migration will give a SQL like database
    #show name instead of object
    def __str__(self):
        return self.name + ' - ' + self.roll