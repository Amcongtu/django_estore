from django import views
from django.urls import path
from . import views

app_name="customers"

urlpatterns = [
    path('login-pc/',views.customer_pc_login,name="login_pc"),
    path('register-pc/',views.customer_pc_register,name="register_pc"),
    path('logout-pc/',views.customer_pc_logout,name="logout_pc"),
    path('my-account/',views.my_account,name="my-account"),
    
]


