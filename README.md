# Entrega__proyecto-final
Entrega de mi Proyecto Final - Coder

En esta entrega del proyecto final se accede a un blog en internet que permite ver, crear, actualizar y borrar post sobre viajes. Para ello es necesario tener un usuario y contraseña, para loguearse. Usuarios no registrados solamente pueden ver posteos, no tienen la posibilidad de crear uno nuevo. Asimismo, los usuarios registrados tendrán la posibilidad de modificar sus datos personales, su imagen de perfil y enviar mensajes.

Para poder correr el proyecto se debe ingresar a Visual Studio Code y tener instalado Python. Asimismo, se deben correr los siguientes comandos: "python manage.py migrate" y "python manage.py shell < seed_data.py". Finalmente con "python manage.py runserver" ya podemos abrir el navegador, ingresar a localhost8000 y veremos el listado de opciones. En este caso, nos centraremos en las funcionalidades de "viajes-blog".

Ingresando a http://localhost:8000/viajes-blog/ ingresaremos a una página principal con el listado de los posteos realizados. Haciendo click en "leer más" accederemos a un detalle ampliado de cada uno. En el extremos superior derecho podremos dirigirnos al sector de envío de mensajes a través del botón "Contacto", crear un nuevo usuario mediante el botón "Registrarse" o bien ingresar como usuario logueado mediante "Ingresaar".

viajes-blog/listar permite acceder a una lista de todos los posteos realizados; accediando al detalle de cada uno y en caso de ser un usuario identificado teniendo las opciones de actualizarlo o borrarlo.

viajes-blog/crear dirige al apartado para crear un nuevo post. En caso de no estar registrado, el sistema solicita previamente la identificación con usuario y contraseña-

Conociendo el id del post se puede acceder mediante url al detalle, actualización y borrado del mismo, reemplazando en las siguientes rutas el "<int:pk>" por el id correspondiente: viajes-blog/<int:pk>/detalle/, viajes-blog/<int:pk>/detalle/, viajes-blog/<int:pk>/actualizar/. En caso de no conocer el número id, desde el apartado listar antes mencionado se acceden a estas opciones.

Asimismo, desde las siguientes url se puede acceder a la registración de un nuevo usuario, al logueo o a cerrar sesión: viajes-blog/signup/, viajes-blog/login/ y viajes-blog/logout/. Estas opciones, como fue mencionado anteriormente, también están disponibles en el marco superior derecho de la página principal, haciendo más amigable la experiencia usuario.

En relación a los mensajes, los usuarios registrados podrán crearlos, verlos y borrarlos. Estas opciones están habilitadas desde la url viajes-blog/users/mensajes/listar/ a través de hipervínculos o bien a traves de cada url en particular: viajes-blog/users/mensajes/crear/, viajes-blog/users/mensajes/<int:pk>/detalle/ y viajes-blog/users/mensajes/<int:pk>/borrar/.

Por otra parte, existe un usuario administrador que es el único en poder crearle a cada usuario su avatar, o foto de perfil. Luego, cada usuario desde viajes-blog/listar/ podrá actualizarlo (seleccionando la opción en el hipervínculo) o bien ingresando en viajes-blog/avatars/<int:pk>/actualizar/ (reemplazando <int:pk> por el número correspondiente a quien se quiere actualizar).

