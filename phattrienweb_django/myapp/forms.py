from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Articles


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(required=True)
    password1 = forms.CharField(
        label="Password", required=True, widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password", required=True, widget=forms.PasswordInput
    )


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles  # Chỉ định model sử dụng cho form
        fields = ["header", "body", "user"]

    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=True)
        | User.objects.filter(is_superuser=True),
        required=True,
    )
