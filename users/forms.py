from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from .models import CustomUser


# TODO: разберись для чего они нужны
class CustomUserCreationForm(UserCreationForm):
    """Хуй знает для чего """

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'username',)


# TODO: разберись для чего они нужны
class CustomUserChangeForm(UserChangeForm):
    """Хуй знает для чего """

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username',)


class UsersFormUpdate(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('image', 'username', 'first_name', 'last_name')
        labels = {'username': 'Ник'}
        help_texts = {'username': 'Обезат. поле'}
