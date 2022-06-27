from unicodedata import name
from django.urls import  path
from . import views

urlpatterns = [
    #url del sitio en este caso el home
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros')
]