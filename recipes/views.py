from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.recipe_factory import *
from recipes.models import Recipe
from django.http import Http404

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(is_published = True).order_by('-id')
    return render(request,'recipes/pages/home.html', context={
        'recipes':recipes,
    })

def category(request,category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404('Not Dound :(')
    else:
        return render(request,'recipes/pages/category.html', context={
            'recipes':recipes,
        })




def recipes(request,id):
    return render(request,'recipes/pages/recipe-view.html', context={
        'recipe':make_recipe(),
        'is_datail_page':True,
    })
