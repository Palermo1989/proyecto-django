from django.shortcuts import render

# Create your views here.pyt
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola, mundo!") 