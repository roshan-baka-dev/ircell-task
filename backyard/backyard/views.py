# I have made this file - Roshan Ekka 
import re
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def data(request):
    return HttpResponse("DataBase are shown here")

def about(request):
    return HttpResponse("About")