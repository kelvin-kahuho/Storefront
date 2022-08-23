from audioop import reverse
from random import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *
from django.core import serializers
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    products = Product.objects.all()[:6]

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

    
    

    from api.views import recommended_products

    recommended_products = recommended_products



    import random
    products = Product.objects.all()
    products = random.choices(products, k=3)[:3]

    return render(request, 'store/product.html', {
        "recommended_products": recommended_products,
        "products": products,
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
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    rating = data['rating']
    print('rating:', rating)
    print('ProductId:', productId)
    user = request.user
    productId = Product.objects.get(id=productId)

    productRating, created = ProductRating.objects.get_or_create(user=user, product=productId, rating=rating)
    productRating.save()
    return JsonResponse('Rating was added', safe=False)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password not correct')
            return render(request, 'store/login.html')
        
    else:
        return render(request, 'store/login.html')

def signupUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Customer.objects.create(user=user, name=username, email=None)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {
        'form': form
        })

def logoutUser(request):
    logout(request)
    return redirect('login')

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
