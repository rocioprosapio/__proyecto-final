"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import monstrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, mostrar_viajes, BuscarViaje, ViajesCrear, ViajesBorrar, ViajesActualizar, mostrar_compras, BuscarCompra, ComprasCrear, ComprasBorrar, ComprasActualizar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/alta', AltaFamiliar.as_view()), # NUEVA RUTA PARA ALTA FAMILIAR
    # EL paramatro pk hace referencia al identificador único en la base de datos para Familiar.
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), # NUEVA RUTA PARA ACTUALIZAR FAMILIAR
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()), # NUEVA RUTA PARA BORRAR FAMILIAR
    path('panel-viajes/', mostrar_viajes),
    path('panel-viajes/buscar', BuscarViaje.as_view()),
    path('panel-viajes/alta', ViajesCrear.as_view()),
    path('panel-viajes/borrar/<int:pk>/', ViajesBorrar.as_view()),
    path('panel-viajes/actualizar/<int:pk>/', ViajesActualizar.as_view()),
    path('panel-compras/', mostrar_compras),
    path('panel-compras/buscar', BuscarCompra.as_view()),
    path('panel-compras/alta', ComprasCrear.as_view()),
    path('panel-compras/borrar/<int:pk>/', ComprasBorrar.as_view()),
    path('panel-compras/actualizar/<int:pk>/', ComprasActualizar.as_view()),
]

