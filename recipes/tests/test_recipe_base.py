from django.contrib.auth.models import User
from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase (TestCase):

    def setUp(self) -> None:
        category = Category.objects.create(name='category')
        author = User.objects.create_user(
            first_name='User',
            last_name='Usuario',
            username='Usename',
            password='24446666688888888',
            email='elivelton@gemeu.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='recipe Title',
            description='uma descrição para recipe',
            slug='simplesmente-uma-slug',
            preparation_time=10,
            preparation_time_unity='mulheres',
            servings=2,
            servings_unit='moças',
            preparation_steps='mode de fazer desta recita porra',
            preparation_steps_is_html=False,
            is_published=True,
        )
        return super().setUp()
