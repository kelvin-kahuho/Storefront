from ast import Str
from time import timezone
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User
import math



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
	
	def averagerating(self):
			rating = ProductRating.objects.filter(product=self).aggregate(avarage=Avg('rate'))
			avg=0
			if review["avarage"] is not None:
					avg=float(review["avarage"])
			return avg

	def countreview(self):
			reviews = ProductRating.objects.filter(product=self).aggregate(count=Count('id'))
			cnt=0
			if reviews["count"] is not None:
					cnt = int(reviews["count"])
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





