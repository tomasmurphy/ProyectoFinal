
import http
from django.shortcuts import render, redirect, HttpResponse
from AppProyectoFinal.models import *
from AppProyectoFinal.forms import *


def inicio(request):
     
      m1 = Perfil.objects.all()[0]
      m2 = m1.book()
      
      return render(request, "AppProyectoFinal/inicio.html",m2)

def galeria(request):
      m1=Obra.objects.all()

      diccionario = {"imagen":m1}

      return render(request, "AppProyectoFinal/galeria.html",diccionario)

def mensajes(request):
      m1=Contacto.objects.all()

      diccionario = {"mensaje":m1}

      return render(request, "AppProyectoFinal/mensajes.html",diccionario)

def bio(request):
      m1 = Bio.objects.all()[0]
      m2 = m1.__str__()
      return render(request, "AppProyectoFinal/bio.html",m2)

def cv(request):
      m1=Curso_Muestra.objects.all()
      return render(request, "AppProyectoFinal/curriculum.html",{"cv":m1})

def ingresar(request):
      
      return render(request, "AppProyectoFinal/ingresar.html")
           
def buscarmensaje(request):
      
      return render(request, "AppProyectoFinal/buscarmensaje.html") 

def buscar(request):
      if request.GET["nombre"]:
            nombre = request.GET["nombre"]
            mensaje = Contacto.objects.filter(nombre__icontains=nombre)
            return render(request, "AppProyectoFinal/resultadobusqueda.html",{"nombre":nombre,"mensaje":mensaje})
      else:
            return render(request, "AppProyectoFinal/mensajes.html")
  
def pag_no_econtrada(request, exception):
    
    return render(request, "AppProyectoFinal/404.html", status=404)

# def error500(request, exception):
    
#     return render(request, "AppProyectoFinal/404.html", status=500)

# FORMULARIOS

def form_bio(request):
      if request.method == "POST":
            mi_form_bio = Form_bio(request.POST)
            print(mi_form_bio)
            if mi_form_bio.is_valid():
                  informacion = mi_form_bio.cleaned_data
                  bio = Bio(bio = informacion["bio"])
                  bio.save()
                  return redirect("ingresar")
      else:
            mi_form_bio = Form_bio()
      return render(request, "AppProyectoFinal/form_bio.html", {"mi_form_bio":mi_form_bio})

def form_obra(request):
      if request.method == "POST":
            mi_form_obra = Form_obra(request.POST, request.FILES)
            print(mi_form_obra)
            if mi_form_obra.is_valid():
                  informacion = mi_form_obra.cleaned_data
                  obra = Obra(imagen= informacion["imagen"],nombre= informacion["nombre"],anio= informacion["anio"])
                  obra.save()
                  return redirect("ingresar")
      else:
            mi_form_obra = Form_obra()
      return render(request, "AppProyectoFinal/form_obra.html", {"mi_form_obra":mi_form_obra})

def form_perfil(request):
            if request.method == "POST":
                  mi_form_perfil = Form_perfil(request.POST, request.FILES)
                  print(mi_form_perfil)
                  if mi_form_perfil.is_valid():
                        informacion = mi_form_perfil.cleaned_data
                        perfil = Perfil(nombre_del_blog= informacion["nombre_del_blog"],profesion= informacion["profesion"],img_fondo= informacion["img_fondo"])
                        perfil.save()
                        return redirect("ingresar")
            else:
                  mi_form_perfil = Form_perfil()
            return render(request, "AppProyectoFinal/form_perfil.html", {"mi_form_perfil":mi_form_perfil})

def contacto(request):
            if request.method == "POST":
                  mi_form_contacto = Form_contacto(request.POST, request.FILES)
                  print(mi_form_contacto)
                  if mi_form_contacto.is_valid():
                        informacion = mi_form_contacto.cleaned_data
                        contacto = Contacto(nombre= informacion["nombre"],email= informacion["email"],mensaje= informacion["mensaje"])
                        contacto.save()
                        return redirect("contacto")
            else:
                  mi_form_contacto = Form_contacto()
            return render(request, "AppProyectoFinal/contacto.html", {"mi_form_contacto":mi_form_contacto})
 
def form_curso(request):
            if request.method == "POST":
                  mi_form_curso = Form_curso_muestra(request.POST, request.FILES)
                  print(mi_form_curso)
                  if mi_form_curso.is_valid():
                        informacion = mi_form_curso.cleaned_data
                        curso = Curso_Muestra(nombre= informacion["nombre"],fecha= informacion["fecha"],lugar= informacion["lugar"],sitio_web_lugar= informacion["sitio_web_lugar"])
                        curso.save()
                        return redirect("ingresar")
            else:
                  mi_form_curso = Form_curso_muestra()
            return render(request, "AppProyectoFinal/form_curso.html", {"mi_form_curso":mi_form_curso})
       