
from shop.models import Category,Product
from rest_framework import serializers


class getAllProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name']

class jsonSearch(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
   