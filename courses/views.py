from django.shortcuts import render
from .servises import *
from .models import Course

sort_positions = {
    'рейтингу': 'rating',
    'авторам': 'author',
    'сложности': 'level',
    'дате создания': 'created',
}


def index(request):
    return render(request, 'courses/index.html', context={"object": "Главная страница курсов"})


def all_courses(request):

    if request.POST:
        fillters = request.POST.get('filtration')
        all_object_courses = fillter(
            object=Course.objects,
            filter=fillters
        )
    else:
        all_object_courses = all_object(object=Course.objects)

    context = {
        "title": "Список все курсы",
        'all_object_courses': all_object_courses,
        'sort_positions': sort_positions,

    }
    return render(request, 'courses/all_courses.html', context=context)


def follower_courses(request):
    return render(request, 'courses/follower_courses.html', context={"object": "Курсы на которые подписаны"})


def create_courses(request):
    return render(request, 'courses/create_courses.html', context={"object": "создание курсов"})
