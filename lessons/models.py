from django.db import models
from dictionaries.models import EnglishWord
from courses.models import Course


class Lesson(models.Model):
    """Модель урока"""
    title = models.CharField(max_length=75, verbose_name='Название')
    words = models.ManyToManyField(EnglishWord, verbose_name='Слова')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['-created']
