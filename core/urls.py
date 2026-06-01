from django.urls import path
from .views import home, galeria, contacto, formulario_cliente, formulario_mascota, listado_mascota, nueva_mascota, modificar_mascota, eliminar_mascota, registro_usuario

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name="galeria"),
    path('contacto/', contacto, name="contacto"),
    path('formulario_cliente/', formulario_cliente, name="formulario_cliente"),
    path('formulario_mascota/', formulario_mascota, name="formulario_mascota"),
    path('listado-mascota/', listado_mascota, name="listado_mascota"),
    path('nueva-mascota/', nueva_mascota, name="nueva_mascota"),
    path('modificar-mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('registro/', registro_usuario, name='registro_usuario'),
   
   ]