#from django.db import models

# Create your models here.
from djongo import models


# Create your models here.

    
# Modelo de Datos de Ordenes
class ordenes(models.Model):
    folioTicket = models.IntegerField(primary_key=True, verbose_name='Folio Ticket', null = False, default = '5422590')
    fechaSolicitud = models.DateField(null=False, verbose_name='Fecha Solicitud', default='20-04-2020')
    horaSolicitud = models.TimeField(null=False,verbose_name='Hora Solicitud', default='11:39:00')
    nombreSolicitante = models.CharField(max_length=100, verbose_name='Nombre Solicitante', null=False, default='Carlos Boza' )
    telefono = models.IntegerField(verbose_name='Telefono', null=True, default='229759700')
    email = models.EmailField(verbose_name='Email', default='cboza@pjud.cl')
    id_ubicacion = models.ForeignKey( "ubicaciones", on_delete=models.CASCADE, verbose_name='Ubicacion')
    direccion = models.CharField(max_length=100, blank=True, default='direccion')
    id_equipoReportado = models.ForeignKey("modeloEquipos", on_delete=models.CASCADE, verbose_name='Modelo Reportado')
    serieReportada = models.CharField(max_length=50, verbose_name='Serie Reportada')
    ipReportada = models.CharField(max_length=20, verbose_name='IP Reportada')
    contratoReportado = models.ForeignKey('proyectos', on_delete=models.CASCADE, verbose_name='Proyecto')
    # id_equipoBackup = models.ForeignKey("modeloEquipos", on_delete=models.CASCADE)
    # serieBackup = models.CharField(max_length=50, verbose_name='Serie Backup', blank=True)
    # ipBackup = models.CharField(max_length=20, verbose_name='Ip Backup')     
    # contratoBackup = models.ForeignKey('proyectos', on_delete=models.CASCADE)
    fechaSoporte = models.DateField(blank=True, verbose_name='Fecha Soporte', default='20-04-2020')
    horaSoporte = models.TimeField(blank=True, verbose_name='Hora Soporte', default='13:00:00')
    descripcionSoporte = models.TextField(max_length=255, verbose_name='Descripcion Soporte', blank=True)
    id_solucionCorta = models.ForeignKey('soluciones', on_delete=models.CASCADE, verbose_name='Solucion Corta')
    solucionDetalle = models.TextField(max_length=255, verbose_name='Solucion Detallada', blank=True)  
    fechaTermino = models.DateField(blank=True, verbose_name='Fecha Termino', default='20-04-2020')
    horaTermino = models.TimeField(blank=True, verbose_name='Hora Termino', default='15:00:00')
    responsable = models.CharField(max_length=50, blank=True, verbose_name='Responsable', default='Responsable')
    id_especialista = models.ForeignKey('especialistas', on_delete=models.CASCADE, verbose_name='Especialista')
    orden_docum = models.FileField(verbose_name='Orden de Trabajo', blank=True)

    def __int__(self):
        return self.folioTicket
    
    

# Informaticos

class informaticos(models.Model):
    
    nombreInformatico = models.CharField(max_length=100, verbose_name="Nombre Informatico", default='Juan Diaz', null=False)
    fonoInformatico = models.IntegerField(verbose_name='Telefono', null=False, default='56912345678')
    tribunalInformatico = models.ForeignKey( "ubicaciones", on_delete=models.CASCADE, verbose_name='Tribunal')
    emailInformatico = models.CharField(max_length=100, verbose_name="Email")
    
    def __str__(self):
        return "Nombre: " + self.nombreInformatico + " - Telefono: " + self.fonoInformatico + " - Tribunal: " + self.tribunalInformatico + " - Email: " + self.emailInformatico


# Modelos Complementarios

# Ubicaciones
class ubicaciones(models.Model):
    ubicacion = models.CharField(max_length=100, verbose_name='Ubicacion')
    
    def __str__(self):
        return self.ubicacion

# Equipos 
class modeloEquipos(models.Model):
    modeloEquipo = models.CharField(max_length=100, verbose_name='Modelo')
    
    def __str__(self):
        return self.modeloEquipo

# Proyectos
class proyectos(models.Model):
    nombreProyecto = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombreProyecto

# Soluciones
class soluciones(models.Model):
    descripcionCorta = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcionCorta

# Tecnicos
class especialistas(models.Model):
    
    nombreTecnico = models.CharField(max_length=50, verbose_name='Nombre Tecnico',default='John Doe', null=False)
    residenciaTecnico = models.CharField(max_length=30, verbose_name='Residencia', default='CAPJ', null=False)
    
    
    def __str__(self):
        filaTecnicos = " -  Nombre Tecnico: " + self.nombreTecnico + " - Residencia: " + self.residenciaTecnico
        return filaTecnicos
    