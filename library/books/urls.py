from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
     path('books/', views.filter, name='filter'),
     path("add/", views.add, name='add')
]