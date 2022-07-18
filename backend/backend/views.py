#I have created this file
import email
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse ("index")
    

def data(request):
    name_list = []
    dob_list = []
    roll_list = []
    email_list = []
    pass_list = []
    # get the text
    feed = request.GET.get('name', 'default')
    feed1 = request.GET.get('dob', 'default')
    feed2 = request.GET.get('roll', 'default')
    feed3 = request.GET.get('email', 'default')
    feed4 = request.GET.get('password', 'default')
    print(feed)

    studentname = feed
    dob = feed1
    roll = feed2
    email = feed3
    password = feed4

    name_list.append(studentname+'  ')
    dob_list.append(dob+'  ')
    roll_list.append(roll+'  ')
    email_list.append(email+'  ')
    pass_list.append(password+'  ')

    # analyze the text
    # return HttpResponse ("This is the DataBase page")
    params = {'name' : name_list, 'dob' : dob_list , 'roll': roll_list, 'email' : email_list, 'password' : pass_list}
    
    

    


    

    return render(request, 'data.html', params)


def about(request):
    return HttpResponse ("i am 1roshanekka")
    