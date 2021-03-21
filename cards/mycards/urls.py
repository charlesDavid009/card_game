from django.urls import path, include
from . import views

urlpatterns = [
    path('cards/', views.RandomView.as_view()),
]