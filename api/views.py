from statistics import correlation
from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from store.models import ProductRating, Product, Customer
from store.views import product
from .serializers import ProductRatingSerializers


# Create your views here.


import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 

class Recommendations(viewsets.ModelViewSet): 
    queryset = ProductRating.objects.all() 
    serializer_class = ProductRatingSerializers

df = pd.DataFrame(list(ProductRating.objects.all().values('user', 'product', 'rating')))

def recommendations(df):
    try:
        model=pickle.load(open("model_pkl", 'rb'))
        decompsed_matrix = model.fit_transform(df)
        correlation_matrix = np.corrcoef(decompsed_matrix)
        product = X.index[product]
        correlation_product = correlation_matrix[product]
        recommended_products = X.index[correlation_product > 0.90]
        recommended_products[0:10]
        return recommended_products
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 
