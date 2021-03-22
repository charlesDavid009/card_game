from django.urls import path, include
from . import views

urlpatterns = [
    path('card/',  views.button),
    path('cards/', views.js_random, name= "script"),
    path('xor/', views.xorshift, name= "scripts"),
]
