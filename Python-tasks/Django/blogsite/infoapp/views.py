from django.shortcuts import render
from django.http.response import HttpResponse

def contact(request):
    return render(request, 'info/contact.html')

    
def about(request):
    return render(request, 'info/about.html')
