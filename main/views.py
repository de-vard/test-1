from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required  # Проверяет авторизован ли пользователь
def index(request):
    """Перенести в основной объект"""
    """Просмотр курсов на которые подписан пользователь"""

    return render(request, '_base.html')
