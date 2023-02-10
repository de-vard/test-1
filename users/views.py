from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView

from .models import CustomUser
from .forms import UsersFormUpdate


class UsersDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Класс показывает подробную информацию об пользователе"""
    model = CustomUser
    template_name = 'users/users_main.html'
    login_url = 'account_login'  # перенаправляет пользователя если не он авторизирован
    context_object_name = 'my_users'

    def test_func(self):  # Наследуется от UserPassesTestMixin проверка пользователя
        """ Проверка, что бы пользователь мог редактировать только себя"""
        return self.model.objects.get(pk=self.kwargs["pk"]) == self.request.user


class UsersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Класс удаления пользователя"""
    model = CustomUser
    template_name = 'users/users_delete.html'
    success_url = reverse_lazy('account_login')  # перенаправляет пользователя когда он удалил свою учётку
    login_url = 'account_login'  # перенаправляет пользователя если не он авторизирован
    context_object_name = 'my_users'

    def test_func(self):  # Наследуется от UserPassesTestMixin проверка пользователя
        """ Проверка, что бы пользователь мог редактировать только себя"""
        return self.model.objects.get(pk=self.kwargs["pk"]) == self.request.user


class UsersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Класс редактирования пользователя"""
    model = CustomUser

    labels = {'username': 'Ник'}
    help_texts = {'username': 'Обезат. поле'}
    template_name = 'users/users_update.html'
    login_url = 'account_login'  # перенаправляет пользователя если не он авторизирован
    form_class = UsersFormUpdate  # Указываем использовать свою форму
    context_object_name = 'my_users'

    def test_func(self):  # Наследуется от UserPassesTestMixin проверка пользователя
        """ Проверка, что бы пользователь мог редактировать только себя"""
        return self.model.objects.get(pk=self.kwargs["pk"]) == self.request.user
