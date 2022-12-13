from django.shortcuts import render, get_object_or_404 # <----- Nuevo import
from ejemplo.models import Familiar, Viajes, Compras
from ejemplo.forms import Buscar, BuscarViajes, BuscarCompras, FamiliarForm, ViajesForm, ComprasForm # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


def index(request):
    return render(request, "ejemplo/saludar.html")

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscarfamiliares.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})


class AltaFamiliar(View):
    
    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
    
    
class ActualizarFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/actualizar_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
        form.save()
        msg_exito = f"Se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form, 
                                                    'familiar': familiar,
                                                    'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})
  
  
class BorrarFamiliar(View):
    template_name = 'ejemplo/familiares.html'
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})
    
def mostrar_viajes(request):
    lista_viajes = Viajes.objects.all()
    return render(request, "ejemplo/viajes.html", {"lista_viajes": lista_viajes})

class BuscarViaje(View):
    form_class = BuscarViajes
    template_name = 'ejemplo/buscarviajes.html'
    initial = {"destino":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            destino = form.cleaned_data.get("destino")
            lista_viajes = Viajes.objects.filter(destino__icontains=destino).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_viajes':lista_viajes})
        return render(request, self.template_name, {"form": form})


class ViajesCrear(CreateView):
      model = Viajes
      template_name = 'ejemplo/altaviaje_form.html'
      success_url = "/panel-viajes"
      fields = ["destino", "transporte", "cantidad_dias"]


class ViajesBorrar(DeleteView):
      model = Viajes
      template_name = 'ejemplo/eliminarviajes_delete.html'
      success_url = "/panel-viajes"

class ViajesActualizar(UpdateView):
      model = Viajes
      template_name = 'ejemplo/altaviaje_form.html'
      success_url = "/panel-viajes"
      fields = ["destino", "transporte", "cantidad_dias"]
      

def mostrar_compras(request):
    lista_compras = Compras.objects.all()
    return render(request, "ejemplo/compras.html", {"lista_compras": lista_compras})

class BuscarCompra(View):
    form_class = BuscarCompras
    template_name = 'ejemplo/buscarcompras.html'
    initial = {"descripcion":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            descripcion = form.cleaned_data.get("descripcion")
            lista_compras = Compras.objects.filter(descripcion__icontains=descripcion).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_compras':lista_compras})
        return render(request, self.template_name, {"form": form})

class ComprasCrear(CreateView):
    model = Compras
    template_name = 'ejemplo/altacompra_form.html'
    success_url = "/panel-compras"
    fields = ["articulo", "descripcion", "sucursal", "unidades"]

class ComprasBorrar(DeleteView):
      model = Compras
      template_name = 'ejemplo/eliminarcompras_delete.html'
      success_url = "/panel-compras"

class ComprasActualizar(UpdateView):
      model = Compras
      template_name = 'ejemplo/altacompra_form.html'
      success_url = "/panel-compras"
      fields = ["articulo", "descripcion", "sucursal", "unidades"]