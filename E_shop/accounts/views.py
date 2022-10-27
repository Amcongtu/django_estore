from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,"accounts/index.html",{
        
    })
def login(request):
    
    return render(request,"accounts/user/login.html",{
        
    })
def signup(request):
    
    return render(request,"accounts/user/signup.html",{
        
    })