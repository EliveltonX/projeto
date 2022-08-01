from unittest import skip

from django.urls import resolve, reverse
from recipes import views

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

    def test_recipe_home_not_load_not_published(self):
        """Test if recipes is_published=False dont show anywere"""

        self.make_recipe(is_published=False)
        response = self.client.get(reverse('myRecipes:home'))
        self.assertIn(
            'Nenhuma Receita Cadastrada!',
            response.content.decode('utf-8'),
        )

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

    def test_category_loads_recipes(self):
        needed_tittle = 'Category Test'
        self.make_recipe(title=needed_tittle)

        response = self.client.get(reverse('myRecipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_tittle, content)

    def test_recipe_category_not_load_not_published(self):
        """Test if recipes is_published=False dont show anywere"""
        # need one recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse(
            'myRecipes:recipe', kwargs={'id': recipe.category.id})
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

    def test_recipe_detail_loads_correct_recipe(self):
        needed_tittle = 'this is a detail page - loads one recipe'

        # Need a recipe for this test
        self.make_recipe(title=needed_tittle)

        response = self.client.get(reverse('myRecipes:recipe', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_tittle, content)

    @skip('Test de skip')
    def test_one_test_to_skip(self):
        response = self.client.get(
            reverse('myRecipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_not_load_not_published(self):
        """Test if recipes is_published=False dont show anywere"""
        # need one recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse(
            'myRecipes:recipe', kwargs={'id': recipe.id})
        )
        self.assertEqual(response.status_code, 404)
