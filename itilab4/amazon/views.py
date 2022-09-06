from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloworld(request):
    return HttpResponse("hello world");
def mywebsite(request):
    return HttpResponse("<h1>iti website</h1>");
def sayhello(request,name):
    return HttpResponse(f"<h1>iti website say hello {name} </h1>");
def amazonhome(request):
    return render(request,"amazon/home.html")
    #return HttpResponse("this my amazon home");
def amazonproducts(request):
    products=[
        {"id":1,"name":"mobile","image":'p1.png'},
        {"id": 2, "name": "laptop", "image": 'p2.png'},
        {"id": 3, "name": "playstation5", "image": 'p3.png'}]
    content={"products":products}
    return render(request, "amazon/productsindex.html",content)
    #return HttpResponse(products)