from dataclasses import field
from contact.models import *
from shop.models import Category,Product
from rest_framework import serializers


class getAllLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class getAllCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class jsonSearch(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
   