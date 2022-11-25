from distutils.command.config import dump_file
from django.core import serializers
from statistics import correlation
from rest_framework.decorators import api_view 
from django.core import serializers 
from .models import ProductRating, Product, Customer
from .serializers import ProductRatingSerializers
import pickle
from sklearn import preprocessing 
import pandas as pd 
import numpy as np

class Recommendations(viewsets.ModelViewSet): 
        queryset = ProductRating.objects.all() 
        serializer_class = ProductRatingSerializers

def recommendations(df, product_id):
    model=pickle.load(open("store/recommendation_system/model_pkl", 'rb'))
    decompsed_matrix = model.fit_transform(df)
    correlation_matrix = np.corrcoef(decompsed_matrix)
    correlation_productid = correlation_matrix[product_id]
    recommended_products = df.index[correlation_productid > 0.90]
    recommended_products = list(recommended_products[:3])
    return recommended_products

