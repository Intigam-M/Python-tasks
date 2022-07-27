from django.shortcuts import render
from django.http.response import HttpResponse



def post(request):
    return render(request, 'post.html')

def postDetal(request):
    return render(request, 'post-detal.html')

