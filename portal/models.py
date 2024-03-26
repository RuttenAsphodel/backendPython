from djongo import models
#from django.db import models

# Create your models here.

#Modelo Contrato de Equipos
class contratosEquipos(models.Model):
    
    serie =  models.CharField(max_length=30, verbose_name='Serie', default='MXL9123KS1',null=False, primary_key=True)
    ubicacion = models.CharField(max_length=100, verbose_name='Ubicacion',default='Corte De Apelaciones De Arica',null=False)
    tipo_equipo = models.CharField(max_length=40, verbose_name='Tipo', default='Computador', null=False)
    marca_modelo = models.CharField(max_length=40, verbose_name='Modelo', default='Hp - Prodesk 600g4',null=False)
    contrato = models.CharField(max_length=14, verbose_name='Contrato', default='Pjud4_Anexo3', null=False)

    def __str__(self):
        filaContrato = "Serie: " + self.serie + " - Ubicacion: " + self.ubicacion + " - Tipo Equipo: " + self.tipo_equipo + " - Modelo: " + self.marca_modelo + " - Contrato: " + self.contrato
        return filaContrato
    
# Modelo de Control de Spares
class equiposSpare(models.Model):
    
    folioTicket = models.IntegerField(verbose_name='Folio', default='654321',null=False, primary_key=True)
    estado = models.CharField(max_length=20, verbose_name='Estado',default='Pendiente Retiro')
    tipo = models.CharField(max_length=12, verbose_name='Tipo', default='PC',null=False)
    serie = models.CharField(max_length=25, verbose_name='Serie', default='MXL9123KS1',null=False)
    modelo = models.CharField(max_length=30, verbose_name='Modelo', default='HP Prodesk 600 G4',null=False)
    fechaRetiro = models.DateField(blank=True,default='2023-06-10')
    transporte = models.CharField(max_length=25, verbose_name='Transporte', null=True)
    observaciones = models.CharField(max_length = 40, verbose_name='Observaciones', default='Pendiente Despacho')
    
    def __str__(self):
        filaSpare = "Folio: " + str(self.folioTicket) + " -  Estado: " + self.estado + " - Tipo: " + self.tipo + " - Serie: " + self.serie + " - Modelo: " + self.modelo + " - Fecha Retiro: " + str(self.fechaRetiro) + " - Transporte: " + self.transporte + " - Observaciones: " + self.observaciones
        return filaSpare
    
# Modelo de Tecnicos Residentes
class tecnicoResidente(models.Model):
    
    id = models.AutoField(primary_key=True)
    runTecnico = models.CharField(default="12345678-9", max_length=13, verbose_name='Rut Tecnico')
    nombreTecnico = models.CharField(max_length=50, verbose_name='Nombre Tecnico',default='John Doe', null=False)
    residenciaTecnico = models.CharField(max_length=30, verbose_name='Residencia', default='CAPJ', null=False)
    
    
    def __str__(self):
        filaTecnicos = "Rut Tecnico: " + self.runTecnico + " -  Nombre Tecnico: " + self.nombreTecnico + " - Residencia: " + self.residenciaTecnico
        return filaTecnicos
    
