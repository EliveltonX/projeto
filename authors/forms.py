from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):

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

    if 'atenção' in data:
        raise ValidationError(
            'Não digite atenção no campo password',
            code='invalid',
            params={'value': 'atenção'}
        )

    return data
