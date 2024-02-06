from typing import Any

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput

User = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields["email"].label = "Your Email Adress"
        self.fields["email"].required = True
        self.fields["username"].label = "Your Username"
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email=email).exists() and len(email) > 254:
            raise forms.ValidationError("Email already in use ot too long")
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=PasswordInput(attrs={"class": "form-control"}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields["email"].label = "Your Email Adress"
        self.fields["email"].required = True

    class Meta:
        model = User
        fields = ["username", "email"]
        exclude = ("password1", "password2")
