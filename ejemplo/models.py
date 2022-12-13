from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    destino_visitado = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.destino_visitado}, {self.id}"
    

class Viajes(models.Model):
    destino = models.CharField(max_length=300)
    transporte = models.CharField(max_length=300)
    cantidad_dias = models.IntegerField()
    
    def __str__(self):
        return f"{self.destino}, {self.transporte}, {self.cantidad_dias}, {self.id}"
    

class Compras(models.Model):
    articulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    sucursal = models.CharField(max_length=300)
    unidades = models.IntegerField()
    
    def __str__(self):
        return f"{self.articulo}, {self.descripcion}, {self.sucursal}, {self.unidades}, {self.id}"