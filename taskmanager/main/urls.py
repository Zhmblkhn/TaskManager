from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # Пустая строка представляет собой переход на главную страницу
    path('about', views.about, name='about'),
]
