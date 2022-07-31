from audioop import reverse
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.core import serializers
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def home(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    products = Product.objects.all()

    if request.user.is_authenticated:
        cartItems = items.count()
    else:
        cartItems = 0

    return render(request, 'store/home.html', {
        "products": products,
        "cartItems": cartItems
    })

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    products = Product.objects.all()

    if request.user.is_authenticated:
        cartItems = items.count()
    else:
        cartItems = 0

    return render(request, 'store/store.html', {
        "products": products,
        "cartItems": cartItems
    })


def product(request, product_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    product = Product.objects.get(pk=product_id)

    if request.user.is_authenticated:
        cartItems = items.count()
    else:
        cartItems = 0

    return render(request, 'store/product.html', {
        "product": product,
        "cartItems": cartItems
    })


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    if request.user.is_authenticated:
        cartItems = items.count()
    else:
        cartItems = 0
        
    context = {'items': items, 'order': order, "cartItems": cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    print(request)
    data = json.loads(request.body)
    print(data)
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

def product_rating(request):
    print(request)
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    rating = data['rating']
    print('rating:', rating)
    print('Product:', productId)
    user = request.body.user.customer
    productId = Product.objects.get(id=productId)

    productRating, created = ProductRating.objects.get_or_create(User=user, Product=productId, Rating=rating)
    productRating.save()
    return JsonResponse('Rating was added', safe=False)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'store/home.html')
        else:
            messages.error(request, 'Username or password not correct')
            return render(request, 'store/login.html')
        
    else:
        return render(request, 'store/login.html')
def signupUser(request):
    return render(request, 'store/signup.html')

def logoutUser(request):
    logout(request)
    return render(request, 'store/login.html')

def dashboard(request):

    return render(request, 'store/dashboard.html', {
        "data": send_data

    })

# method that sends the response with data


def send_data(request):
    dataset = ProductRating.objects.all()
    print(dataset)
    data = serializers.serialize('json', dataset)
    return JsonResponse(request, data, safe=False)
