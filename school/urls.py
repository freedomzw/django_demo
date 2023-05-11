from django.urls import path

from . import views

urlpatterns = [
    path('study/index/', views.index),
]
