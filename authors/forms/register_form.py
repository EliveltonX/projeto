from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_attr, add_placeholder, strong_password


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'your username')
        add_placeholder(self.fields['email'], 'your Email')
        add_placeholder(self.fields['password'], '*****')
        add_placeholder(self.fields['first_name'], 'ex: John')
        add_placeholder(self.fields['last_name'], 'ex: Wick')
        add_attr(self.fields['username'], 'css', 'a-css-class')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placehoder': 'Sua senha'
        }),
        error_messages={
            'required': 'password nao pode estar vazio'
        },
        help_text=(
            'Precisa tem uma letra min uma maiuscula e pelomenos 8'
        ),
        validators=[
            strong_password
        ]
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeate your password'
        }),
        label='Confirme Sua Senha',
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atencao' in data:
            raise ValidationError(
                'Não digite %(value)s no campo password',
                code='invalid',
                params={'value': 'atencao'}
            )
        return data

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if 'jhon wick' in data:
            raise ValidationError(
                'Não digite %(value)s no campo first name',
                code='invalid',
                params={'value': 'jhon wick'}
            )
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError('Este email já esta em uso!')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': ValidationError(
                    'password not match diferent',
                    code='invalid'
                ),
                'password2': 'password not match',
            })
