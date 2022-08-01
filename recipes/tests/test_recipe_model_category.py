from unicodedata import category, name

from django.forms import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelCategoryTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='category testinging'
        )
        return super().setUp()

    def test_recipe_category_model_string_representation(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )

    def test_recipe_category_model_max_legth_is_65chars(self):
        self.category.name = 'a'*66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
