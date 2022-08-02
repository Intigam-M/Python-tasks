from django.shortcuts import redirect, render
from .models import Blog
from .forms import ContactForm

def blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'post.html', {'blog':blog})

def home(request):
    blogs = Blog.objects.filter(show = True).order_by('-updated')[:5]
    return render(request, 'index.html', context={'blogs':blogs})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')    


def contact_submit(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  
    else:
        return redirect('contact')        



