from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('welcome', views.welcome, name='welcome'),
    path('tecnicos', views.listadoTecnicos, name='tecnicos'),
    path('spares', views.equiposSpares, name='spares'),
    path('contratos', views.contratoEquipos, name='contratos'),
    
    
    # urls Ordenes
    
    # urls Contratos
    path('contratos/crearcontrato', views.crearContrato, name='crearcontrato'),
    path('contratos/editarcontrato/<str:serie>', views.editarContrato, name='editarcontrato'),
    path('borrarcontrato/<str:serie>', views.borrarContrato, name='borrarcontrato'),
    
    # urls Spares
    path('spares/crearspare', views.crearSpare, name='crearspare'),
    path('spares/editarspare/<int:folioTicket>', views.editarSpare, name='editarspare'),
    path('borrarspares/<int:folioTicket>', views.borrarSpare, name='borrarspare'),
    
    # urls Tecnicos
    path('tecnicos/creartecnico', views.crearTecnico, name='creartecnico'),
    path('tecnicos/editartecnico/<int:id>', views.editarTecnico, name='editartecnico'),
    path('borrartecnico/<int:id>', views.borrarTecnico, name='borrartecnico'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
