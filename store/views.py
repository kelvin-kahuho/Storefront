from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
  products = Product.objects.all()
  return render(request, 'store/store.html',{
    "products": products
  })

def cart(request):
  context = {}
  return render(request, 'store/cart.html', context)

def checkout(request):
  context = {}
  return render(request, 'store/checkout.html', context)