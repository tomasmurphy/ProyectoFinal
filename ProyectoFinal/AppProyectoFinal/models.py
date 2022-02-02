from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from django.db.models import (
Model, CharField, IntegerField, 
DateField, ImageField, URLField,
EmailField, ForeignKey, CASCADE, TextField)
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class Foro(Model):
    usuario = CharField(max_length=100, null=True, blank=True, default="anonimo")
    mensaje = RichTextField()
    fecha = CharField(max_length=100, null=True, blank=True, default=datetime.now())
    
    def __str__(self):
        return f'self.usuario'
    
    class Meta:
        ordering = ["-id"]

class Blog(Model):
    ruta = FileSystemStorage(location="AppProyectoFinal/static/AppProyectoFinal/img")
    usuario = CharField(max_length=200)
    titulo = CharField(max_length=200)
    autor = CharField(max_length=200)
    fecha = CharField(max_length=100, null=True, blank=True, default=datetime.now() )
    texto = RichTextField(max_length=10000)
    portada = ImageField(storage=ruta)
    
    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return "{self.texto} de {self.usuario}"
    
class Podcast(Model):
    usuario = CharField(max_length=100, null=True, blank=True, default="anonimo")
    link = CharField(max_length=100)
    fecha = CharField(max_length=100, null=True, blank=True, default=datetime.now())
    
    def __str__(self):
        return f'self.usuario'
    
    class Meta:
        ordering = ["-id"]
    

    

    