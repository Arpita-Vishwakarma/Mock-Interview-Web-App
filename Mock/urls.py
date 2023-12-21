"""
URL configuration for Mock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
    Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('interview.urls')),
    path('information/', include('interview.urls')),
    path('Cpp/', include('interview.urls')),
    path('java/', include('interview.urls')),
    path('python/', include('interview.urls')),

    path('clanguage/', include('interview.urls')),
    path('login/', include('interview.urls')),
    path('ragi/', include('interview.urls')),
    path('logout/', include('interview.urls')),
    path('mysql/', include('interview.urls')),
    path('Nodejs/', include('interview.urls')),
    path('js/', include('interview.urls')),
    path('html/', include('interview.urls')),
    path('css/', include('interview.urls')),
    path('clanguage/', include('interview.urls'))
]