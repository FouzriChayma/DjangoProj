from django.urls import path , include 
from . import views

urlpatterns = [
    path('hello/<classe>', views.accueil, name='accueil'),
    path("Person/", include("Person.urls")),
]