from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    def _str_(self):
        return f"{self.nombre} {self.apellido} - {self.email}"


class ContactoFormModel(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    def _str_(self):
        return f"{self.nombre} {self.apellido}"
