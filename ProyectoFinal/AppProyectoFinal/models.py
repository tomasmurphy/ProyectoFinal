from distutils.command.upload import upload
from django.db.models import (
Model, CharField, IntegerField, 
DateField, ImageField, URLField,
EmailField)
from django.core.files.storage import FileSystemStorage


class Curso_Muestra(Model):
    
    nombre= CharField(max_length=200)
    fecha = DateField()
    lugar = CharField(max_length=200)
    sitio_web_lugar= URLField()

class Perfil(Model):
    ruta = FileSystemStorage(location="AppProyectoFinal/static/AppProyectoFinal/img")
    nombre_del_blog= CharField(max_length=200)
    profesion = CharField(max_length=200)
    img_fondo = ImageField(storage=ruta)
    
    class Meta:
        ordering = ["-id"]
    
    def book(self):
        return {"nombre_del_blog":self.nombre_del_blog,"profesion":self.profesion,"img_fondo":self.img_fondo}
    
class Obra(Model):
    ruta = FileSystemStorage(location="AppProyectoFinal/static/AppProyectoFinal/img")
    imagen = ImageField(storage=ruta)
    nombre= CharField(max_length=200)
    anio = IntegerField()
    
    def __str__(self):
        return f'{self.imagen}'
    
class Contacto(Model):
    nombre = CharField(max_length=100)
    email = EmailField()
    mensaje = CharField (max_length=1000)

class Bio(Model):
    bio = CharField(max_length=10000)
    class Meta:
        ordering = ["-id"]
    def __str__(self):
        return {"bio":self.bio}
    
