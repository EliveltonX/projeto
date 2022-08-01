from unicodedata import category, name

from django.forms import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_default(self):
        recipe = Recipe(
            category=self.make_category(name='MinhaaCategoriaaa'),
            author=self.make_author(username='testAuthornamefor_l25'),
            title='Test recipe Title miau',
            description='test description for tests',
            slug='Test_recipe_Title_miau',
            preparation_time=2,
            preparation_time_unity='minas',
            servings=2,
            servings_unit='moças',
            preparation_steps='test de models isso is a test modafocka',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand(
        [
            ('title', 65),
            ('description', 165),
            ('preparation_time_unity', 65),
            ('servings_unit', 65),
        ]
    )
    def test_recipe_fields_max_legth(self, field, max_lengh):
        setattr(self.recipe, field, 'A'*(max_lengh+1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_RecipePreparationStepsIsHtmlIsFalseByDefault(self):
        recipe = self.make_recipe_no_default()

        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='||recipe preparation_steps_is_html is not False!||',
        )

    def test_RecipeIsPublished_IsFalseByDefault(self):
        recipe = self.make_recipe_no_default()

        self.assertFalse(
            recipe.is_published,
            msg='||recipe is_published is not False!||',
        )

    def test_recipeString_representation_self(self):
        needded = 'testing representation'
        self.recipe.title = needded
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), needded,
            msg='||Recipe string representation must be "{needed}"||')
