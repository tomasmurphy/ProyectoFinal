from email import charset
from django.forms import *


class Form_bio(Form):
    bio= CharField()

class Form_obra(Form):
    imagen = ImageField()
    nombre = CharField()
    anio = IntegerField()
    
class Form_perfil(Form):
    nombre_del_blog= CharField()
    profesion = CharField()
    img_fondo = ImageField()
    
class Form_curso_muestra(Form):
    
    nombre= CharField(max_length=200)
    fecha = DateField()
    lugar = CharField(max_length=200)
    sitio_web_lugar= URLField()

class Form_contacto(Form):
    nombre = CharField(max_length=100)
    email = EmailField()
    mensaje = CharField (max_length=1000)

    