from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsCategoryTest (RecipeTestBase):

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
