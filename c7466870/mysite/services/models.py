from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services_images/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug}) 
    
class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class SpecialOffer(models.Model):
    title = models.CharField(max_length=100)
    services = models.ManyToManyField(Service, related_name='special_offers')
    discount_percentage = models.FloatField()
    valid_until = models.DateField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    service = models.ForeignKey(Service,  on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service.name}"
