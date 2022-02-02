from django.urls import path, include
from django.urls import path
from AppProyectoFinal import views
from AppProyectoFinal.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #PAGINA PRINCIPAL
    path('', views.inicio, name="inicio"),
    path('login', views.login_request, name="login"),
    path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(template_name="AppProyectoFinal/logout.html"), name="logout"),
    path('acerca_de_mi', views.acerca_de_mi, name="acerca_de_mi"),
    path('ckeditor', include('ckeditor_uploader.urls')),
    #BLOG
    path('galeria', views.GaleriaListView.as_view(), name="galeria"),
    path('ver_blog/(<pk>', views.GaleriaDetailView.as_view(), name="ver_blog"),
    path('blog', views.BlogListView.as_view(), name="blog"),
    path('ver_blog/<pk>', views.BlogDetailView.as_view(), name="ver_blog"),
    path('form_blog', views.BlogCreateView.as_view(), name="form_blog"),
    path('buscar_blog', views.buscar_blog, name="buscar_blog"),
    #FORO
    path('foro', views.ForoListView.as_view(), name="foro"),
    path('mensajes', views.ForoCreateView.as_view(), name="mensajes"),
    path('buscar_mensaje', views.buscar_mensaje, name="buscar_mensaje"),
    #PODCAST
    path('podcast', views.PodcastListView.as_view(), name="podcast"),
    path('form_podcast', views.PodcastCreateView.as_view(), name="form_podcast"),
    path('buscar_podcast', views.buscar_podcast, name="buscar_podcast"),
    #ADMINISTRADOR
    path('administrador', views.administrador, name="administrador"),
    #foro
    path('foro_lista_administrador', views.AdminstradorForoListView.as_view(), name="foro_lista_administrador"),
    path('buscar_mensaje_administrador', views.buscar_mensaje_administrador, name="buscar_mensaje_administrador"),
    path('foro_borrar_administrador/<pk>', views.AdministradorForoDeleteView.as_view(), name="foro_borrar_administrador"),
    path('foro_editar_administrador/<pk>', views.AdministradorForoUpdateView.as_view(), name="foro_editar_administrador"),
    #blog
    path('blog_lista_administrador', views.AdminstradorBlogListView.as_view(), name="blog_lista_administrador"),
    path('buscar_blog_administrador', views.buscar_blog_administrador, name="buscar_blog_administrador"),
    path('blog_borrar_administrador/<pk>', views.AdministradorBlogDeleteView.as_view(), name="blog_borrar_administrador"),
    path('blog_editar_administrador/<pk>', views.AdministradorBlogUpdateView.as_view(), name="blog_editar_administrador"),
    #podcast
    path('podcast_lista_administrador', views.AdminstradorPodcastListView.as_view(), name="podcast_lista_administrador"),
    path('buscar_podcast_administrador', views.buscar_podcast_administrador, name="buscar_podcast_administrador"),
    path('podcast_borrar_administrador/<pk>', views.AdministradorPodcastDeleteView.as_view(), name="podcast_borrar_administrador"),
    path('podcast_editar_administrador/<pk>', views.AdministradorPodcastUpdateView.as_view(), name="podcast_editar_administrador"),
    #usuario
    path('usuario_lista_administrador', views.AdminstradorUserListView.as_view(), name="usuario_lista_administrador"),
    path('buscar_user_administrador', views.buscar_user_administrador, name="buscar_user_administrador"),
    path('usuario_borrar_administrador/<pk>', views.AdministradorUserDeleteView.as_view(), name="usuario_borrar_administrador"),
    path('usuario_editar_administrador/<pk>', views.AdministradorUserUpdateView.as_view(), name="usuario_editar_administrador"),
    path('change_password_administrador/<id>', views.change_password_administrador, name='change_password_administrador'),
    #PERFIL DE USUARIO
    path('editar_usuario', views.UserAutoUpdateView.as_view(), name="editar_usuario"),
    path('mi_usuario', views.mi_usuario, name="mi_usuario"),
    path('change_password', views.change_password, name='change_password'),
    
]
