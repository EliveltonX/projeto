
from django.urls import path
from . import views

app_name = 'myRecipes'

urlpatterns = [
    path('',views.home, name="home"), #Home
    path('recipes/<int:id>/',views.recipes,name="recipe"), #recipes
]
