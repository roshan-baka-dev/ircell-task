##ATENTION MF
# THIS FILE IS MADE MANUALLY INSIDE THE BACKEND 

from django.contrib import admin
from django.urls import path, include

from private import views

#admin customization
admin.site.site_header = 'Welcome Boss'
admin.site.site_title = 'DataBase International Relation Cell'
admin.site.index_title = 'Welcome'



urlpatterns = [
    path('', views.index, name='index'),
    # path('data', views.data, name='data'),

    #delete this shit if made a dynamic page
    path('all', views.all, name='all'),
    path('north_america', views.north_america, name='north-america'),
    path('south_america', views.south_america, name='south_america'),
    path('asia', views.asia, name='asia'),
    path('europe', views.europe, name='europe'),
    path('australia', views.australia, name='australia'),


    path('register', views.register, name='register'),
    
    path('success', views.success, name='success'),
    
    path('about', views.about, name='about'),
    path('base', views.base, name='base'),
    
    # path('', views.index, name='index'),
    #this has to be configured in the views folder as we are deriving from that folder
]
