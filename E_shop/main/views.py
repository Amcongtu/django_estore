from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,"main/index.html",{
        "nav":"index",
    })

def detail(request):
    
    return render(request,"main/detail.html",{
        "nav":"index",
    })


def shop(request):
    
    return render(request,"main/shop.html",{
        "nav":"shop",
    })

def error(request,exception):
        
    return render(request,"main/error404.html",{
        "nav":"error",
    })

def error500(request):
        
    return render(request,"main/error404.html",{
        "nav":"error",
    })