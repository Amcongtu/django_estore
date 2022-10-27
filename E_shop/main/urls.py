from django import views
from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('',views.index,name="index"),

    path('jsonlocation/',views.getJsonLocationBase.as_view(),name="getJsonLocationBase"),
    path('jsoncategory/',views.getJsonCategoryBase.as_view(),name="getJsonCategory"),
    path('search-topnav/',views.search,name="search"),
]


