from django.urls import path
from . import views

urlpatterns = [
    path('hello/<classe>', views.accueil, name='accueil'),
]