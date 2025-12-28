from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # Пустая строка представляет собой переход на главную страницу
    path('about', views.about)
]
