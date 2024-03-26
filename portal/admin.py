from django.contrib import admin
from .models import contratosEquipos
from .models import equiposSpare
from .models import tecnicoResidente

# Register your models here.
admin.site.register(contratosEquipos)
admin.site.register(equiposSpare)
admin.site.register(tecnicoResidente)