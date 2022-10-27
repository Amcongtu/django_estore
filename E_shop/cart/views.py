from django.shortcuts import render

# Create your views here.
def cart(request):
    
    return render(request,"cart/cart.html",{
        "nav":"cart",
    })
def checkout(request):
    return render(request,"cart/checkout.html",{
        "nav":"checkout",
    })