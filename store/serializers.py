from rest_framework import serializers 
from store.models import ProductRating

class ProductRatingSerializers(serializers.ModelSerializer): 
    class meta: 
        model= ProductRating 
        fields='__all__'