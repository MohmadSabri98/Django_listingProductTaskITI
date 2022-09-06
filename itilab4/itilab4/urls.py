"""itilab4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
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
from django.urls import path,include
from amazon.views import helloworld,mywebsite,sayhello
from books.views import booksindex

urlpatterns = [
    path('admin/', admin.site.urls),
    #create my first url amzon.views
#     path('hello',helloworld),
#     path('mywebsite',mywebsite),
# path('mywebsite/<name>',sayhello)
    # books.views
path('amazon/',include("amazon.urls")),
    # path("bookindex",booksindex)
path('books/',include("books.urls")),
]
