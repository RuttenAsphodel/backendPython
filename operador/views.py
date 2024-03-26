from django.shortcuts import render, redirect
from .models import ordenes, informaticos, ubicaciones, especialistas, proyectos, modeloEquipos, soluciones
from .forms import ordenesForm, informaticosForm

# Create your views here.
# Vista de Ordenes
def ordenesTrabajo(request):
    dataordenes = ordenes.objects.all()
    
    # obtener el valor del formulario de búsqueda si existe
    # nTicket_query = request.GET.get('nTicket')
    # if series_query:
    #     equipos = equipos.filter(serie__icontains=series_query)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(equipos, 20)
    
    # try:
    #     equipos = paginator.page(page)
    # except PageNotAnInteger:
    #     equipos = paginator.page(1)
    # except EmptyPage:
    #     equipos = paginator.page(paginator.num_pages)
        
    
    return render(request, 'ordenes/listadoordenes.html', {'dataordenes': dataordenes})

def crearOrden(request):
    formularioOrden = ordenesForm(request.POST or None)
    if formularioOrden.is_valid():
        formularioOrden.save()
        formularioOrden = ordenesForm()
            
    context = {
        'formularioOrden':formularioOrden
    }
    return render(request, 'ordenes/nuevaorden.html', context)

# def editarOrden(request, folioTicket):
#     formularioOrden = ordenes.objects.get(folioTicket=folioTicket)
#     formularioOrden = ordenes(request.POST or None, instance=formularioOrden)
#     if formularioOrden.is_valid():
#         formularioOrden.save()
#         return redirect('ordenes')
#     return render(request, 'ordenes/editarorden.html', {'formularioOrden': formularioOrden})

# def borrarOrden(request, folioTicket):
#     formularioOrden = ordenes.objects.get(folioTicket=folioTicket)
#     formularioOrden.delete()
#     return redirect('ordenes')  


# Ver Listado de Informaticos
def verInformaticos(request):
    dataInformaticos = informaticos.objects.all()
    
    # obtener el valor del formulario de búsqueda si existe
    # nTicket_query = request.GET.get('nTicket')
    # if series_query:
    #     equipos = equipos.filter(serie__icontains=series_query)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(equipos, 20)
    
    # try:
    #     equipos = paginator.page(page)
    # except PageNotAnInteger:
    #     equipos = paginator.page(1)
    # except EmptyPage:
    #     equipos = paginator.page(paginator.num_pages)
        
    
    return render(request, 'informaticos/listadoinformatico.html', {'dataInformaticos': dataInformaticos})


# Crear Informatico
def crearInformatico(request):
    formularioInformaticos = informaticosForm(request.POST or None)
    if formularioInformaticos.is_valid():
        formularioInformaticos.save()
        formularioInformaticos = informaticosForm()
            
    context = {
        'formularioInformaticos':formularioInformaticos
    }
    return render(request, 'informaticos/nuevoinformatico.html', context)

# Ver Listado de Informaticos
def verInformaticos(request):
    dataInformaticos = informaticos.objects.all()
    
    # obtener el valor del formulario de búsqueda si existe
    # nTicket_query = request.GET.get('nTicket')
    # if series_query:
    #     equipos = equipos.filter(serie__icontains=series_query)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(equipos, 20)
    
    # try:
    #     equipos = paginator.page(page)
    # except PageNotAnInteger:
    #     equipos = paginator.page(1)
    # except EmptyPage:
    #     equipos = paginator.page(paginator.num_pages)
        
    
    return render(request, 'informaticos/listadoinformatico.html', {'dataInformaticos': dataInformaticos})
