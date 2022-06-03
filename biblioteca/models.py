from encodings import CodecRegistryError
from django.db import models

# Create your models here.
class Autor(models.Model):
    idAutor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

class Libro(models.Model):
    idLibro = models.IntegerField(primary_key=True)
    idAutor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    codigo = models.IntegerField()
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    numPags = models.IntegerField()

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    numUsuario = models.IntegerField()
    nif = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

class Prestamos(models.Model):
    idPrestamo = models.IntegerField()
    idLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecPrestamo = models.DateField()
    fecDevolucion = models.DateField()

