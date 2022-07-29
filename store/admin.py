from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Customer)
@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name','email']
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
#admin.site.register(ProductRating)

@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['get_users', 'product', 'rating']