from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('AppProyectoFinal.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
 
]

handler404 = "AppProyectoFinal.views.error404"
handler500 = "AppProyectoFinal.views.error500"