from django.contrib import admin

from lessons.admin import LessonInline
from .models import Course


# todo: Закончи админку в курсах и уроках

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Класс курсов"""

    def save_model(self, request, obj, form, change):
        """ Для автоматического определения
            пользователя и сохранения его как автора
        """
        obj.author = request.user
        super().save_model(request, obj, form, change)

    inlines = [
        LessonInline,
    ]
    list_display = ('level', 'title', 'created', 'updated', 'author')
    list_editable = ('title',)
    search_fields = ('title',)
    exclude = ('author',)
