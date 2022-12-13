# pre-entrega__proyecto-final
Pre-entrega de mi Proyecto Final - Coder

La pre-entrega cuenta con tres clases en models:
 - Familiares
 - Viajes
 - Compras

Si bien por el momento las funcionalidades operan de manera independiente entre sí, el proyecto busca tener en una página web el registro de los viajes realizados por familiares y las compras realizadas en cada destino para cuando uno empieza a armar las valijas de su próximo destino! 
Acá se podrán conocer, entre otras cosas, el transporte utilizado, los días destinados a conocer el lugar, las compras realizadas y los recuerdos que se pueden traer, además de tener de referencia el familiar que fue para poder hacerle todas las consultas necesarias!

Al correr el proyecto desde la terminal abrimos en el navegador el localhost:8000
Allí podremos observar un listado de opciones para cada clase: buscar, dar de alta, actualizar y eliminar de ser necesario. Asimismo, al ingresar al listado de cada clase (a través de "mi-familia/", "panel-viajes/" y/o "panel-compras/") se puede acceder a las funcionalidades de dar de alta un nuevo familiar, viaje y/o compra y además por cada registro ya realizado se puede acceder a la actualización o eliminación.
Estas funcionalidades también son accedidas a través del buscador con por ejemplo "/mi-familia/alta", "/panel-viajes/borrar/<int:pk>/", "panel-compras/actualizar/<int:pk>/", o la que corresponda según lo que se desea realizar.
En caso de no acordarnos dónde fue cada familiar, cuántos días destinar a cada destino o qué cosas comprar en las vacaciones ¡No hay problema! Contamos con un buscador para hacerlo más sencillo: para ello, ingresar en "mi-familia/buscar" con el nombre del familiar, o en "panel-viajes/buscar" con el destino visitado, o en "panel-compras/buscar" con el producto que se esté tratando de conseguir para saber dónde comprarlo.

Hay veces que organizar un viaje es complejo, por eso con este proyecto quiero aportar facilidades a la hora de organizar y también nuevas ideas para viajar!

Los viajes comienzan desde que nos sentamos a planearlo :)
