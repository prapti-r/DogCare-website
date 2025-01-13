from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import BlogPost, Category

def blog_list(request):
    posts = BlogPost.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts, 'categories': categories})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    categories = Category.objects.all()
    return render(request, 'blog/blog_detail.html', {'post': post, 'categories': categories})


