from django.shortcuts import render
from .models import Blog

def blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'post.html', {'blog':blog})

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')    
