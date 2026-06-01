from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=800, null=True, blank=True)
    color = models.CharField(max_length=20)
    peso = models.IntegerField()
    fecha_nacimiento_mascota = models.DateField()
    imagen = models.FileField(null=True, blank=True)
  

    def __str__(self):
        return self.nombre

class Raza(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Slider(models.Model):
    imagen = models.ImageField()

class GL(models.Model):
    foto = models.ImageField() 

class Mision(models.Model):
    descripcion = models.CharField(max_length=2000)

     
    
class TipoMascota(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre
     

class Dueño(models.Model):
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
     