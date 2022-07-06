from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request):
  context = {}
  return render(request, 'store/store.html',{
    "products": Product.objects.all()
  })

def cart(request):
  context = {}
  return render(request, 'store/cart.html', context)

def checkout(request):
  context = {}
  return render(request, 'store/checkout.html', context)