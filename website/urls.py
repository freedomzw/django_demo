from django.urls import path

from . import views

urlpatterns = [
    path('articles/login/', views.login),
    path('articles/index/', views.index),
    path('articles/publisher_list/', views.publisher_list),
    path('articles/add_publisher/', views.add_publisher),
    path('articles/edit_publisher/', views.edit_publisher),
    path('articles/del_publisher/', views.del_publisher),
]
