# Entrega__proyecto-final
Entrega de mi Proyecto Final - Coder

Este proyecto final consiste en un Blog de Viajes al que se accede por internet y permite ver, crear, actualizar y borrar post sobre lugares de Argentina para conocer. Para operar en el Blog es necesario tener un usuario y contraseña para loguearse. Usuarios no registrados solamente pueden ver posteos, no tienen la posibilidad de crear uno nuevo. Asimismo, los usuarios registrados tendrán la posibilidad de modificar sus datos personales, su imagen de perfil y enviar mensajes. Las funcionalidades de alta de un nuevo usuario, inicio de sesión y cierre de la misma tamnbién forman parte del proyecto.

Para poder correr el proyecto es necesario tener instalado Python, Git, Visual Studio Code y django.
Para instalar Python se debe acceder a https://www.python.org/ ir al apartado de descargas y seleccionar el sistema operativo de la PC donde se va a estar trabajando; luego deben seguir los pasos indicados en la página. Se recomienda tener instalada la versión 3.8 o superior; para chequearlo, se debe correr "python --version" o "py --version".
Para instalar Git se debe acceder a https://git-scm.com/ y descargar el paquete correspondiente al sistema operativo que posea la PC. Para el caso de windows: se ejecuta el archivo descargado y se elige la ruta de guardado; es necesario tener seleccionada la herramienta "git bash" en el proceso de instalación. Se debe elegir la opción “use visual studio code as Git’s default editor” y se finaliza con las configuraciones por defecto. Para el caso de mac: en preferencias de seguridad se selecciona "abrir de todos modos" al momento de ejecutar el archivo descargado; luego click en "abrir" y "continuar" hasta finalizar la isntalación.
Para instalar Visual Studio Code acceder a https://code.visualstudio.com/download y seleccionar la descarga según el sistema operativo.
Para instalar django: acceder a www.djangoproject.com y descargar la última o anteúltima versión (en el caso de windows se puede instalar bajo el comando pip install Django desde el cmd o desde la terminal de VCS).

Por otra parte, en la terminal de VSC se deben correr los siguientes comandos: "python manage.py migrate" y "python manage.py shell < seed_data.py". 
Finalmente con "python manage.py runserver" ya podemos abrir el navegador, ingresar a localhost8000 y veremos el listado de opciones. En este caso, nos centraremos en las funcionalidades de "viajes-blog".

Ingresando a http://localhost:8000/viajes-blog/ ingresaremos a una página principal con el listado de los posteos realizados. Haciendo click en "leer más" accederemos a un detalle ampliado de cada uno. En el extremos superior derecho podremos dirigirnos al sector de envío de mensajes a través del botón "Contacto", crear un nuevo usuario mediante el botón "Registrarse" o bien ingresar como usuario logueado mediante "Ingresaar".

viajes-blog/listar permite acceder a una lista de todos los posteos realizados; accediando al detalle de cada uno y en caso de ser un usuario identificado teniendo las opciones de actualizarlo o borrarlo.

viajes-blog/crear dirige al apartado para crear un nuevo post. En caso de no estar registrado, el sistema solicita previamente la identificación con usuario y contraseña.

Conociendo el id del post se puede acceder mediante url al detalle, actualización y borrado del mismo, reemplazando en las siguientes rutas el "<int:pk>" por el id correspondiente: viajes-blog/<int:pk>/detalle/, viajes-blog/<int:pk>/detalle/, viajes-blog/<int:pk>/actualizar/. En caso de no conocer el número id, desde el apartado listar antes mencionado se acceden a estas opciones.

Asimismo, desde las siguientes url se puede acceder a la registración de un nuevo usuario, al logueo o a cerrar sesión: viajes-blog/signup/, viajes-blog/login/ y viajes-blog/logout/. Estas opciones, como fue mencionado anteriormente, también están disponibles en el marco superior derecho de la página principal, haciendo más amigable la experiencia usuario.

En relación a los mensajes, los usuarios registrados podrán crearlos, verlos y borrarlos. Estas opciones están habilitadas desde la url viajes-blog/users/mensajes/listar/ a través de hipervínculos o bien a traves de cada url en particular: viajes-blog/users/mensajes/crear/, viajes-blog/users/mensajes/<int:pk>/detalle/ y viajes-blog/users/mensajes/<int:pk>/borrar/.

Por otra parte, existe un usuario administrador que es el único en poder crearle a cada usuario su avatar, o foto de perfil. Luego, cada usuario desde viajes-blog/listar/ podrá actualizarlo (seleccionando la opción en el hipervínculo) o bien ingresando en viajes-blog/avatars/<int:pk>/actualizar/ (reemplazando <int:pk> por el número correspondiente a quien se quiere actualizar).

Para ver el video mostrando cómo funciona el proyecto se debe acceder al siguiente link: https://youtu.be/do0F03dRHpM

Muchas gracias!