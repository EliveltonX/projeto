from authors.forms import RegisterForm
from django.test import TestCase
# from django.test import TestCase as DjangoTestCase
from django.urls import reverse
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):

    @parameterized.expand([
        ('username', 'your username'),
        ('email', 'your Email'),
        ('password', '*****'),
        ('first_name', 'ex: John'),
        ('last_name', 'ex: Wick'),
    ])
    def test_fields_place_holder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('password', 'Precisa tem uma letra min uma maiuscula e pelomenos 8'),
    ])
    def test_fields_help_test(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)


class AuthorRegisterFormIntegrationTest(TestCase):
    def setUp(self, *args, **kwargs) -> None:
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@email.com',
            'password': 'Str0ngP@assw0rd1234',
            'password2': 'Str0ngP@assw0rd1234',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('username', 'Este campo é obrigatório.'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
