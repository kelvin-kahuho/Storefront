from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Customer)
@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name','email']

#admin.site.register(Product)
@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ['name','price','gender','stock_status']


#admin.site.register(Order)
@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ['customer','date_ordered','complete','transaction_id']


#admin.site.register(OrderItem)
@admin.register(OrderItem)
class orderitemAdmin(admin.ModelAdmin):
    list_display = ['product','order','quantity','date_added']


#admin.site.register(ShippingAddress)
@admin.register(ShippingAddress)
class shippingaddressAdmin(admin.ModelAdmin):
    list_display = ['customer','order','address','city','state','zipcode','date_added']


#admin.site.register(ProductRating)

@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'created_at', 'comment']