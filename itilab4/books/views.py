from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booksindex(request):
    return HttpResponse("<h1>book index</h1>")
def bookshome(request):
    return render(request,"books/home.html")