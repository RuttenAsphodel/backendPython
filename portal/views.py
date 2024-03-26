from django.shortcuts import render,redirect
from .models import contratosEquipos,equiposSpare,tecnicoResidente
from .forms import tecnicoForm, spareForm, contratoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# Pantallas de inicio
def inicio(request):
    return render(request, 'base.html')

def welcome(request):
    return render(request, 'navegacion/welcome.html')


# Views Ordenes

# Views Spares
def equiposSpares(request):
       
    dataspare = equiposSpare.objects.all()
    
    spare_query = request.GET.get('observaciones')
    if spare_query:
        dataspare = dataspare.filter(observaciones__icontains=spare_query)
     
    return render(request, 'spares/listadospare.html',{'dataspare':dataspare})


def crearSpare(request):
    formularioSpare = spareForm(request.POST or None)
    if formularioSpare.is_valid():
        formularioSpare.save()
        return redirect('spares')
    return render(request, 'spares/crearspare.html', {'formularioSpare': formularioSpare})

def editarSpare(request, folioTicket):
    dataspare = equiposSpare.objects.get(folioTicket=folioTicket)
    formularioSpare = spareForm(request.POST or None, instance=dataspare)
    if formularioSpare.is_valid():
        formularioSpare.save()
        return redirect('spares')
    return render(request, 'spares/crearspare.html', {'formularioSpare': formularioSpare})

def borrarSpare(request, folioTicket):
    dataspare = equiposSpare.objects.get(folioTicket=folioTicket)
    dataspare.delete()
    return redirect('spares')   

# Views Tecnicos 
def listadoTecnicos(request):
    datatecnico = tecnicoResidente.objects.all()
    return render(request, 'tecnicos/listadotecnico.html',{'datatecnico':datatecnico})

def crearTecnico(request):
    formularioTecnico = tecnicoForm(request.POST or None)
    if formularioTecnico.is_valid():
        formularioTecnico.save()
        return redirect('tecnicos')
    return render(request, 'tecnicos/creartecnico.html', {'formularioTecnico': formularioTecnico})

def editarTecnico(request,id):
    datatecnico = tecnicoResidente.objects.get(id=id)
    formularioTecnico = tecnicoForm(request.POST or None, instance=datatecnico)
    if formularioTecnico.is_valid() and request.POST:
        formularioTecnico.save()
        return redirect('tecnicos')    
    return render(request, 'tecnicos/editartecnico.html', {'formularioTecnico': formularioTecnico})
    

def borrarTecnico(request, id):
    datatecnico = tecnicoResidente.objects.get(id=id)
    datatecnico.delete()
    return redirect('tecnicos')   


# Views Contratos

def contratoEquipos(request):
    equipos = contratosEquipos.objects.all()
    
    # obtener el valor del formulario de búsqueda si existe
    series_query = request.GET.get('series')
    if series_query:
        equipos = equipos.filter(serie__icontains=series_query)

    page = request.GET.get('page', 1)
    paginator = Paginator(equipos, 20)
    
    try:
        equipos = paginator.page(page)
    except PageNotAnInteger:
        equipos = paginator.page(1)
    except EmptyPage:
        equipos = paginator.page(paginator.num_pages)
        
    
    return render(request, 'contratos/listadocontratos.html', {'equipos': equipos})

def crearContrato(request):
    formularioContrato = contratoForm(request.POST or None)
    if formularioContrato.is_valid():
        formularioContrato.save()
        return redirect('contratos')
    return render(request, 'contratos/crearcontrato.html', {'formularioContrato': formularioContrato})

def editarContrato(request, serie):
    datacontrato = contratosEquipos.objects.get(serie=serie)
    formularioContrato = contratoForm(request.POST or None, instance=datacontrato)
    if formularioContrato.is_valid():
        formularioContrato.save()
        return redirect('contratos')
    return render(request, 'contratos/crearspare.html', {'formularioContrato': formularioContrato})

def borrarContrato(request, serie):
    datacontrato = equiposSpare.objects.get(serie=serie)
    datacontrato.delete()
    return redirect('contratos')   