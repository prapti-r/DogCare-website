from django.http import HttpResponse
from django.shortcuts import render
from blog.models import BlogPost, Category

def home(request):
    blogs_posts = BlogPost.objects.all().order_by('-created_at')[:3]  
    return render(request, 'home.html', {'blogs_posts': blogs_posts})

def aboutus(request):
    return render(request, "aboutus.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    blog = blog.objects.all()
    context = {
        'blog': blog,
    }
    return render(request, "blog.html", context)

def blogdetail(request):
    return render(request, "blogdetail.html")





