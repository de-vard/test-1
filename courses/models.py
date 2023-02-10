from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Course(models.Model):
    """Модель курса"""
    CHOICE = (
        ('a', 'Легкий уровень'),
        ('b', 'Средний уровень'),
        ('c', 'Сложный уровень'),
    )
    level = models.CharField(choices=CHOICE, max_length=1, verbose_name='Уровень сложности')
    title = models.CharField(max_length=75, verbose_name='Название', db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования', auto_now=True)
    rating = models.IntegerField('Рейтинг', validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['-created']
