from argparse import Action
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.core import serializers
from .utils import cookieCart, cartData, guestOrder


# Create your views here.
def store(request):
  products = Product.objects.all()
  return render(request, 'store/store.html',{
    "products": products,
    "data": data
  })

def product(request, product_id):
  product = Product.objects.get(pk=product_id)
  return render(request, 'store/product.html', {
    "product": product
  })

def cart(request):
  if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, complete=False)
      items = order.orderitem_set.all()
  else:
      items=[]
      order = {'get_cart_total':0, 'get_cart_items':0}

  context = {'items':items, 'order':order}
  return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def dashboard(request):
    
    return render(request, 'store/dashboard.html',{
      "data" : data

  })

#method that sends the response with data
def data(request):
    dataset = models.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(request, data, safe=False)