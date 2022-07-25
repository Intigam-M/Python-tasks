from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')      