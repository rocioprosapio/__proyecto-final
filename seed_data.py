from ejemplo.models import Familiar
from ejemplo.models import Viajes
from ejemplo.models import Compras


Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123, destino_visitado="Ushuaia").save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890, destino_visitado="Buzios").save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345, destino_visitado="Cordoba").save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567, destino_visitado="Mercedes").save()

Viajes(destino="Buzios", transporte="avion", cantidad_dias=15).save()
Viajes(destino="Fortaleza", transporte="avion", cantidad_dias=11).save()
Viajes(destino="Río de Janeiro", transporte="avion", cantidad_dias=3).save()
Viajes(destino="Colonia", transporte="barco", cantidad_dias=3).save()
Viajes(destino="Bariloche", transporte="avion", cantidad_dias=9).save()

Compras(articulo="mochi", descripcion="mochila con cierres y bolsillos de costado", sucursal="Bariloche", unidades=1).save()
Compras(articulo="tomagic", descripcion="toalla de secado rapido", sucursal="Iguazú", unidades=2).save()
Compras(articulo="dulces", descripcion="alfajores de chocolate", sucursal="Bariloche", unidades=24).save()