from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('', index, name='main'),

    path('all/', all_courses, name='all'),
    path('follower/', follower_courses, name='follower'),
    path('create/', create_courses, name='create'),
]
