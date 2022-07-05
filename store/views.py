from django.shortcuts import render

# Create your views here.
def store(request):
  context = {}
  return render(request, 'assets/shop.html', context)

def cart(request):
  context = {}
  return render(request, 'store/cart.html', context)

def checkout(request):
  context = {}
  return render(request, 'store/checkout.html', context)