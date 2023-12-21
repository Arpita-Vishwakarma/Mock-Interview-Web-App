from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('information/', views.information, name='information'),
    path('questions/', views.questions, name='questions'),
    path('Cpp', views.Cpp, name='Cpp'),
    path('java/', views.java, name='java'),
    path('python/', views.python, name='python'),
    path('clanguage/', views.clanguage, name='clanguage'),
    path('login/', views.login, name='login'),
    path('ragi/', views.ragi, name='ragi'),
    path('logout', views.logout, name='logout'),
    path('mysql', views.mysql, name='mysql'),
    path('Nodejs/', views.Nodejs, name='Nodejs'),
    path('js/', views.Nodejs, name='js'),
    path('html/', views.html, name='html'),
    path('css/', views.css, name='css'),
    path('python/', views.python, name='leranpy'),
    path('clanguage/', views.clanguage, name='clanguage')

]