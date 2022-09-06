

from django.urls import path
from amazon.views import helloworld,mywebsite,sayhello,amazonhome,amazonproducts


urlpatterns = [

   # create my first url amzon.views
    path('hello',helloworld),
    path('mywebsite',mywebsite),
path('mywebsite/<name>',sayhello),
    path('home',amazonhome),
    path('products',amazonproducts)

]
