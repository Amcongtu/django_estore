from django import views
from django.urls import path
from . import views

app_name="shop"

urlpatterns = [
    path('shop/<str:pk>/',views.shop,name="shop"),
    path('shop/detail/',views.detail,name="detail"),
]


