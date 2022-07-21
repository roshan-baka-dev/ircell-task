
import re
from django.shortcuts import render
from django.shortcuts import HttpResponse

from private.models import student
import datetime


# Create your views here.
def index(request):
    # return HttpResponse('This is my home page (/)')
    #hey mann you should return a template not a sada sa text 
    #so we create a template and return it to that template/html page whenever user opens the index server

    #you can pass more info like dictionary from here to html file diretly
    # context = {'name' : 'Roshan', 'place': 'Rourkela'}
    return render(request, 'index.html')
    #this should render the templates file ~ index.html

def register(request):
    if request.method=='POST':
        # print('this is post')
        name = request.POST['name']
        dob = request.POST['dob']
        roll = request.POST['roll']
        email = request.POST['name']
        password = request.POST['password']
        # print(name, dob, roll, email, password)

        ins = student(name=name, dob=dob, roll=roll, email=email, password=password)
        ins.save()
        print('the data of student has been saved on the database. cool!')
        #now this returns the success page
        return render(request, 'success.html')
    else:
        return render(request, 'register.html')
    
    # return HttpResponse('register page (/)')


def about(request):
    return HttpResponse('about page (/)')
# def index(request):
#     return HttpResponse('This is my home page (/)')
# def index(request):
#     return HttpResponse('This is my home page (/)')



##delete if made a JS to make it dynamic
def all(request):
    return render(request, 'index.html')
def north_america(request):
    return render(request, 'north_america.html')
def south_america(request):
    return render(request, 'south_america.html')
def asia(request):
    return render(request, 'asia.html')
def europe(request):
    return render(request, 'europe.html')
def australia(request):
    return render(request, 'australia.html')
    # return HttpResponse('about page (/)')


def success(request):
    return render(request, 'success.html')
    # return HttpResponse('about page (/)')
def base(request):
    return render(request, 'base.html')

def about(request):
    return HttpResponse('about page (/)')