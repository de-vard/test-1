from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()  # ссылаемся на модель пользователя


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Пользовательская модель"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm  # класс формы, на основе которого будет создана окончательная форма
    model = get_user_model()
    list_display = ['id', 'email', 'username']
    # UserAdmin.fieldsets += ('Мои поля', {'fields': ('image',)}), # Код оставил как пример
    UserAdmin.fieldsets[1][1]["fields"] += 'image', 'courses'  # Добавляем поле image из модели CustomUser в админку

