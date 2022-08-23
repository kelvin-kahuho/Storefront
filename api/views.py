from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from store.models import ProductRating 
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

def status(df):
    try:
        scaler=pickle.load(open("/Users/HP-k/DeployML/DjangoAPI/Scaler.sav", 'rb'))
        model=pickle.load(open("/Users/HP-k/DeployML/DjangoAPI/Prediction.sav", 'rb'))
        X = scaler.transform(df) 
        y_pred = model.predict(X) 
        y_pred=(y_pred>0.80) 
        result = "Yes" if y_pred else "No"
        return result 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 
