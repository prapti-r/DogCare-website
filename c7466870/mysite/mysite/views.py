from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from blog.models import BlogPost, Category
from services.models import ServiceCategory
from services.forms import BookingForm

def home(request):
    blogs_posts = BlogPost.objects.all().order_by('-created_at')[:3]  
    categories = ServiceCategory.objects.all()[:4]  
    return render(request, 'home.html', {'categories': categories, 'blogs_posts': blogs_posts})

def aboutus(request):
    return render(request, "aboutus.html")


def services(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'services/services_list.html', {'categories': categories})

def servicedetail(request, category_slug):
    category = get_object_or_404(ServiceCategory, slug=category_slug)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('services_list')

    return render(request, 'services/service_detail.html', {'category': category, 'form': form})


def blog(request):
    blog = blog.objects.all()
    context = {
        'blog': blog,
    }
    return render(request, "blog.html", context)

def blogdetail(request):
    return render(request, "blogdetail.html")


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse("Thank you for your message!")
    return render(request, 'contact.html')


