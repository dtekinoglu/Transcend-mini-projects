from django.urls import path
from random_number import views

urlpatterns = [
    path('', views.random_number, name='random_number'),
]