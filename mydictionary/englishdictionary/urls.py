from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('word_info', views.word_info),
]