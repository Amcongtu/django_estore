from itertools import product
from django.shortcuts import render
from .models import *
# Create your views here.
def shop(request,pk):
    nav = "Shop" 
    products=""
    categories = Category.objects.all()
    if (pk == "all-item"):
        products = Product.objects.filter(status_product=1)
    elif (pk == "clearance-sale"):
        nav = "CLEARANCE SALE"
    else:
        products= Product.objects.filter(category__name=pk)

    return render(request,"shop/shop_main/shop.html",{
        "nav":nav,
        "products":products,
        "categories":categories,
    })


def detail(request):
    return render(request,"shop/detail.html",{
        "nav":"Detail",
       
    })

