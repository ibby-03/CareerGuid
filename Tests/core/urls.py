# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('personality/', views.take_quiz, name='take_quiz'),
    path('quiz_results/', views.quiz_results, name='quiz_results'),
]
