# PrroyectoFinal

*** El proyecto final es la rama proyecto final. La rama master es la preentrega.***

## Tomas Murphy

## BLOG
Es un blog donde se pueden subir reseñas de libros, podcast de spotify e interactuar en un foro.

Video corto de la pagina. 
https://drive.google.com/file/d/1jbVHeN0jcpFlWOqrCan-1wPVEqly-4Js/view?usp=sharing

### Inicio
Se ingresa desde localhost:http://127.0.0.1:8000

### Superusuario
blogcoder / admin123

### Requeriments
Hay un archivo txt lleno de cosas en la carpeta principal. (No todo se usa, me quedó ahi)
El texto enriquecido esta hecho con ckeditor. 

### Sin login
Se puede ingresar sin usuario, cargar reseñas, podcast y mensajes, que se fijan por defecto como anonimo.

### Login
En en el acceso de login se puede inicar sesion o crear un usuario.
Con usuario la carga de podcast, reseñas y mensajes se setea por defecto con el usuario. 
Se agrega en la navbar el nombre de usuario y un acceso a editar su perfil y contraseña(con permiso de usuario). 

El superuser en lugar de acceso a editar perfil tiene acceso al Administrador(Con permiso de administrador), donde puede editar o borrar reseñas, mensajes, podcast u usuarios.
En la edicion de usuarios puede hacerlo parte del staff para que ese usuario sea una especie de moderador, 
accediendo tambien al Administrador. 

*** todos los posteos se orden con -id para que aparezca siempre el ultimo arriba. ***

### Galeria
Carga por defecto la portada del posteo del blog, con autor y titulo (Titulo es un detailview del posteo)

### Reseñas
Hay un acceso a crear tu reseña, un buscador de reseña por titulo y una listview de todas las reseñas. El titulo es un detailview.
*** Las imagenes siguen la ruta = FileSystemStorage(location="AppProyectoFinal/static/AppProyectoFinal/img") dentro del modelo, ya que lo hice antes de aprender el media root. ***

### Podcast
Hay un acceso a crear tu podcast, un buscador de podcast por usuario y una listview de todas las podcasts.
La idea era trabajara con un URLfield para cambiar un poco, pero el codigo de spotify es distinto al de incrustacion. 

### Foro
Hay un buscador de mensaje por usuario, un acceso para dejar tu mensaje y una listview de todos los mensaje.

### Logout
LLeva a un gato que mira.

### Acerca de mi
Esta el acceso en el pie de pagina. 
