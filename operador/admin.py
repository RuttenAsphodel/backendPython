from django.contrib import admin
from .models import ordenes,especialistas,proyectos,soluciones,modeloEquipos, ubicaciones


# Register your models here.
admin.site.register(especialistas)
admin.site.register(proyectos)
admin.site.register(soluciones)
admin.site.register(modeloEquipos)
admin.site.register(ubicaciones)
admin.site.register(ordenes)

