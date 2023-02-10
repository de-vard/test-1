from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import EnglishWord


@admin.register(EnglishWord)
class EnglishWordAdmin(admin.ModelAdmin):
    """Класс английских слов"""
    list_display = ('id', 'title', 'transcription', 'get_image', 'updated', 'created',)
    list_display_links = ('id',)
    list_editable = ('title', 'transcription',)
    search_fields = ('title',)

    save_on_top = True  # Устанавливаем меню и во вверху
    save_as = True  # добавление кнопки "сохранить как новый объект"

    readonly_fields = ('get_image',)  # Добавляем мини изображение в просмотре отдельных слов

    def get_image(self, obj):
        """Получаем мини изображение или ретерним что его нет"""
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width="50" height="60">')
        else:
            return 'Фото отсутствует'

    get_image.short_description = 'Изображения'  # Указываем название мини изображения
