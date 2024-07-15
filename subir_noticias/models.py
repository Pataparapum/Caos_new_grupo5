from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    CATEGORIAS = [
        ('----', '---'),
        ('policial', 'Policial'),
        ('economia', 'Economía'),
        ('deportes', 'Deportes'),
        ('ciencia_tecnologia', 'Ciencia y Tecnología'),
        ('internacional', 'Internacional'),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    ubicacion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    aprobada = models.BooleanField(default=False)
    rechazada = models.BooleanField(default=False)
    motivo_rechazo = models.TextField(blank=True, null=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Imagen(models.Model):
    noticia = models.ForeignKey('Noticia', related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return f"Imagen para {self.noticia.titulo}"