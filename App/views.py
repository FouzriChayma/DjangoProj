from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def accueil(request,classe):
    return HttpResponse("Bonjour <i>"+classe+"</i> !")