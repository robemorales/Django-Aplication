from unicodedata import name
from xml.dom.minidom import Document
from django.urls import  path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    #url del sitio en este caso el home
    path('', views.home, name='home'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('books', views.books, name='books'),
    path('books/add', views.add, name='add'),
    #path('books/edit', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('books/edit/<int:id>', views.edit, name='edit')

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)