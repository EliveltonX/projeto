from recipes.views import *
from django.urls import path

urlpatterns = [
    path('',home),              #Home
    path('sobre/',sobre),       #sobre
    path('contato/',contato),   #contato
]
