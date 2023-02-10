from django.urls import path
from .views import UsersDetailView, UsersDeleteView, UsersUpdateView

app_name = 'my_users'

urlpatterns = [
    path('<int:pk>/', UsersDetailView.as_view(), name='main'),

    path('delete/<int:pk>/', UsersDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', UsersUpdateView.as_view(), name='update')
]
