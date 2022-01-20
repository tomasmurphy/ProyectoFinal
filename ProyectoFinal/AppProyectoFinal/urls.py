from django.urls import path, include
from django.urls import path
from AppProyectoFinal import views

urlpatterns = [
   
    path('', views.inicio, name="inicio"),
    path('galeria', views.galeria, name="galeria"),
    path('bio', views.bio, name="bio"),
    path('curriculum', views.cv, name="curriculum"),
    path('contacto', views.contacto, name="contacto"),
    path('ingresar', views.ingresar, name="ingresar"),
    path('form_obra', views.form_obra, name="form_obra"),
    path('form_perfil', views.form_perfil, name="form_perfil"),
    path('form_bio', views.form_bio, name="form_bio"),
    path('form_curso', views.form_curso, name="form_curso"),
    path('mensajes', views.mensajes, name="mensajes"),
    path('buscar', views.buscar, name="buscar")
]
