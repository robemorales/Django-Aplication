import re
from urllib import request
import django
from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm

from django.http import HttpResponse

from libreria import models

def home(request):
    #permite ante una peticion renderizar a la vista
    return render(request,'pages/index.html')
def nosotros(request):
    return render(request, 'pages/nosotros.html')

def books(request):
    books = Book.objects.all() 
    return render(request, 'books/index.html', {'books': books})
def add(request):
    bookForm = BookForm(request.POST or None, request.FILES or None)
    if bookForm.is_valid():
        bookForm.save()
        return redirect('books')
    return render(request, 'books/add.html', {'formBook': bookForm} )
def edit(request, id):
    #creamos la consulta
    book = Book.objects.get(id = id)
    print(book)
    #recuperar el dato del libro
    bookForm = BookForm (request.POST or None, request.FILES or None, instance=book)
    return render(request, 'books/edit.html', {'bookForm':bookForm})
def delete(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    return redirect('books')         

# Create your views here.
