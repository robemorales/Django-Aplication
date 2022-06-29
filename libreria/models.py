from cgitb import text
from distutils.command.upload import upload
from email.mime import image
from msilib.schema import Class
from statistics import mode
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='Title')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Image')
    description = models.TextField(null=True, verbose_name='Description')

    def __str__(self):
        fila = "Title: "+self.title + " - " + "Description: "+ self.description
        return fila 
    #este codigo se encarga de eliminar la imagen de mi carpeta debido a que, si no lo ejecuto se elimina mi libro pero no se elimina la imagen de la carpeta
    def delete(self, using = None, keep_parents=False):
        self.image.delete(self.image.name)
        super().delete()