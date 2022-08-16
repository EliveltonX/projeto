from unittest.mock import patch

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsHomeTest (RecipeTestBase):

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

    def test_recipe_home_not_load_not_published(self):
        """Test if recipes is_published=False dont show anywere"""

        self.make_recipe(is_published=False)
        response = self.client.get(reverse('myRecipes:home'))
        self.assertIn(
            'Nenhuma Receita Cadastrada!',
            response.content.decode('utf-8'),
        )

    def test_recipe_home_is_paginated(self):
        for i in range(20):
            kwargs = {'slug': f'r{i}',
                      'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)

        with patch('recipes.views.PER_PAGE', new=9):
            response = self.client.get(reverse('myRecipes:home'))
            recipes = response.context['recipes']
            paginator = recipes.paginator
            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 9)
            self.assertEqual(len(paginator.get_page(2)), 9)
            self.assertEqual(len(paginator.get_page(3)), 2)
