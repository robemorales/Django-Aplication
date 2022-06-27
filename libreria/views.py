from urllib import request
import django
from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    #permite ante una peticion renderizar a la vista
    return HttpResponse('<p>HELLO WORLD DJANGO</p>')
def nosotros(request):
    return render(request, 'pages/nosotros.html')    

# Create your views here.
