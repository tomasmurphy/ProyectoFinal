from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('AppProyectoFinal.urls')),
 
]

handler404 = "AppProyectoFinal.views.pag_no_econtrada"
