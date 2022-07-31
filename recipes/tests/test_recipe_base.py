from django.contrib.auth.models import User
from django.test import TestCase
from recipes.models import Category, Recipe


class RecipeTestBase (TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Categoria'):
        return Category.objects.create(name='Category')

    def make_author(
        self,
        first_name='User',
        last_name='Usuario',
        username='Usename',
        password='24446666688888888',
        email='elivelton@gemeu.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
        self,
        category_data=None,
        author_data=None,
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
    ):
        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unity=preparation_time_unity,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )
