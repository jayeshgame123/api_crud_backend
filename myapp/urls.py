from django.contrib import admin
from django.urls import path
from .views import UserView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/<int:pk>/',UserView.as_view()),
]