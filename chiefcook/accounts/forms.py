from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
        self.fields["first_name"].required = True

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "first_name")
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "autocomplete": "email",
                    "placeholder": "Введите email...",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "autofocus": True,
                    "autocomplete": "username",
                    "placeholder": "Придумайте логин...",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "autocomplete": "given-name",
                    "placeholder": "Ваше имя",
                    "required": True,
                }
            ),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Введите логин...",
            }
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "placeholder": "Введите пароль...",
            }
        )
    )
