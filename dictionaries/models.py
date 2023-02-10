from django.core import validators
from django.db import models


class EnglishWord(models.Model):
    """Английское слово"""
    title = models.CharField(max_length=75, verbose_name='Cлово', db_index=True)
    value = models.CharField(max_length=75, verbose_name='Русское значение')
    transcription = models.CharField(max_length=75, blank=True, verbose_name='Транскрипция')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования', auto_now=True)
    irregular_verbs = models.BooleanField(default=False, verbose_name='Не правильный глагол')
    audi = models.FileField(upload_to='audi/%Y/%m/%d', blank=True, verbose_name='Произношение',
                            validators=[validators.RegexValidator(regex=".mp3")], )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
        ordering = ['-created']
