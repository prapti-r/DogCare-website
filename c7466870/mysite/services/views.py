
# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404
from .models import ServiceCategory, SpecialOffer
from .forms import BookingForm
from django.contrib import messages

def services_list(request):
    categories = ServiceCategory.objects.all()
    special_offers = SpecialOffer.objects.all() 

    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('services_list')

    return render(request, 'services/services_list.html', {'categories': categories, 'special_offers': special_offers, 'form': form})

def services_detail(request, slug):
    category = get_object_or_404(ServiceCategory, slug=slug)
    return render(request, 'services/services_detail.html', {'category': category,})

    
