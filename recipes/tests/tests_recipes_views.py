from django.urls import resolve, reverse
from recipes import views
from recipes.models import Recipe

from .test_recipe_base import RecipeTestBase


class RecipeViewsTest (RecipeTestBase):

    # -- HOME --
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('myRecipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_200_OK(self):
        response = self.client.get(reverse('myRecipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('myRecipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('myRecipes:home'))
        self.assertIn(
            'Nenhuma Receita Cadastrada!',
            response.content.decode('utf-8'),
        )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('myRecipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('recipe Title', content)

    # -- Category --

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(
            reverse('myRecipes:category', kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes(self):
        response = self.client.get(
            reverse('myRecipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    # -- Detail --
    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('myRecipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)

    def test_recipe_detail_view_returns_404_if_no_recipes(self):
        response = self.client.get(
            reverse('myRecipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
