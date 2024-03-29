from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsSearchTest (RecipeTestBase):

    # -- Search --

    def test_recipe_search_load_correct_view(self):
        url = reverse('myRecipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('myRecipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_404_if_no_search_term(self):
        response = self.client.get(reverse('myRecipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_title_and_escaped(self):
        url = reverse('myRecipes:search')+'?q=Testando'
        response = self.client.get(url)
        self.assertIn(
            'seach for &quot;Testando&quot;',
            response.content.decode('utf-8')
        )

    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = 'this is recipe one'
        title2 = 'this is recipe two'

        recipe1 = self.make_recipe(
            slug='one',
            title=title1,
            author_data={'username': 'one'}
        )
        recipe2 = self.make_recipe(
            slug='two',
            title=title2,
            author_data={'username': 'two'}
        )

        search_url = reverse('myRecipes:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=this')

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])
        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])
