
# Register your models here.
from django.contrib import admin
from .models import ServiceCategory, Service, SpecialOffer, Booking

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_services', 'discount_percentage', 'valid_until')
    search_fields = ('title',)  
    list_filter = ('valid_until',)

    def get_services(self, obj):
        return ", ".join([service.name for service in obj.services.all()])
    get_services.short_description = 'Services'
    def get_search_results(self, request, queryset, search_term):
        queryset = super().get_search_results(request, queryset, search_term)
        if search_term:
            queryset = queryset.filter(services__name__icontains=search_term).distinct()
        return queryset

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'date', 'time')
    search_fields = ('name', 'service__name')
    list_filter = ('date', 'service')
