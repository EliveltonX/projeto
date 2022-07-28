from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views


class RecipeViewsTest (TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('myRecipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(
            reverse('myRecipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('myRecipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)
