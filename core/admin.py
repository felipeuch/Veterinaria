from django.contrib import admin
from .models import Dueño, TipoMascota, Mascota, Raza, Slider, GL, Mision
# Register your models here.


class DueñoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'telefono']
    search_fields = ['rut', 'nombre', 'apellido', 'telefono']
    list_filter = ['rut']
    list_per_page = 10


class MascotaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'color', 'peso', 'fecha_nacimiento_mascota', 'imagen']
    search_fields = ['nombre']
    list_filter = ['nombre']
    list_per_page = 10

class SliderAdmin(admin.ModelAdmin):
    list_display = ['imagen']
    list_per_page = 10


class GLAdmin(admin.ModelAdmin):
     list_display = ['foto']



class MisionAdmin(admin.ModelAdmin):
     list_display = ['descripcion']



admin.site.register(Dueño, DueñoAdmin)

admin.site.register(Mision, MisionAdmin)

admin.site.register(Slider, SliderAdmin)

admin.site.register(GL, GLAdmin)

admin.site.register(TipoMascota)

admin.site.register(Mascota, MascotaAdmin)

admin.site.register(Raza)


