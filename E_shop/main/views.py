from unicodedata import category
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from contact.models import Location
from shop.models import *
from django.db.models import Q
import random


# Create your views here.

def index(request):
    val_first = random.randint(1, Category.objects.all().count())-1
    number=Category.objects.all().count()-3
    if(val_first>number):
        val_first = number
    val_last = val_first + 3
    product_trendy=Product.objects.all().order_by("create_date")[0:4]

    category_list=Category.objects.all()[val_first:val_last]
    # for item in range(1,4):
    #     category_list.append(Category.objects.get(id=1))
    return render(request,"main/index.html",{
        "nav":"index",
        "categories":category_list,
        "product_trendy":product_trendy,
    })
def error(request,exception):
        
    return render(request,"main/error404.html",{
        "nav":"error",
    })

def error500(request):
        
    return render(request,"main/error404.html",{
        "nav":"error",
    })


# Serializer
from . import serializers

class getJsonLocationBase(APIView):
    def get(self, request):
        locations = Location.objects.all()
        mydata=serializers.getAllLocationSerializer(locations,many=True)
        return Response( data=mydata.data,status = status.HTTP_200_OK)


class getJsonCategoryBase(APIView):
    def get(self, request):
        category = Category.objects.all()
        data=serializers.getAllCategorySerializer(category,many=True)
        return Response( data=data.data,status = status.HTTP_200_OK)


# class search(APIView):
#     # register
#     def get(self, request):
#         keywords=request.GET.get("search-topbar")
#         search = Product.objects.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords))
#         data = jsonSearch(search, many=True)
#         return Response( data=data.data,status = status.HTTP_200_OK)
       


def search(request):
    nav = "Shop" 
    product=""
    categories = Category.objects.all()

    if request.GET.get('search_topnav'):
        keywords = request.GET.get("search_topnav")
        product = Product.objects.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords) \
                                        | Q(material=keywords) | Q(tag__name__icontains=keywords))
    return render(request,"shop/shop_main/shop.html",{
        "nav":nav,
        "products":product,
        "categories":categories,
    })
