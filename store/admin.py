from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
  list_display = ('get_users','Product','Rating')
