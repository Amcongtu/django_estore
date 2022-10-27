from django import views
from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('admin/',views.index,name="index"),
    path('admin/login/',views.login,name="login"),
    path('admin/signup/',views.signup,name="signup"),
 
]


