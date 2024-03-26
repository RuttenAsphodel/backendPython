from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('ordenes', views.ordenesTrabajo,name='ordenes'),
    path('ordenes/nuevaorden', views.crearOrden, name='nuevaorden'),
    path('informaticos',views.verInformaticos, name='informaticos'),
    path('informaticos/nuevoinformatico',views.crearInformatico, name='nuevoinformatico')
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

