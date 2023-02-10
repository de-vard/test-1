from django.contrib import admin
from .models import Lesson


class LessonInline(admin.TabularInline):
    """Класс Уроков"""
    model = Lesson
    extra = 0  # сколько пустых отзывов отображать
