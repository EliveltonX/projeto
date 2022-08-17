from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Ultimo Nome',
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha',
        }
        help_texts = {
            'email': 'Digite um email valido'
        }
