from ast import Str
from time import timezone
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User
import math
from numpy import average, count_nonzero



# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	

	def __str__(self):
		return str(self.name)

	def __str__(self):
  		return str(self.user)



class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)
	description = models.CharField(max_length=1000, null=True, blank=True)
	gender = models.CharField(max_length=6, null=True, blank=True)
	stock_status = models.IntegerField(null=True, blank=True)


	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	@property
	def averagerating(self):
			rating = ProductRating.objects.filter(product=self).aggregate(avarage=average('rating'))
			avg=0
			if rating["average"] is not None:
					avg=float(rating["average"])
			return avg
	@property
	def countrating(self):
			ratings = ProductRating.objects.filter(product=self).aggregate(count=count_nonzero('product_id'))
			cnt=0
			if ratings["count"] is not None:
					cnt = int(ratings["count"])
			return cnt

	def __str__(self):
			return str(self.id)


  
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
	
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

class ProductRating(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	comment = models.CharField(max_length=250, null=True, blank=True)
	rating = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True, null= True, blank=True)

	def __str__(self):
  		return str(self.id)





