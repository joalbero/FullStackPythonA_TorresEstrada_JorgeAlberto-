from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10)
    lugar_residencia = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=100)  # almacenar la contraseña

    def __str__(self):
        return self.nombre_completo
    
class Reporte(models.Model):

    STATUS_CHOICES = (
        ('Pendiente por investigar', 'Pendiente por investigar'),
        ('Investigando', 'Investigando'),
        ('Trabajando en ello', 'Trabajando en ello'),
        ('Solucionado', 'Solucionado'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion_problema = models.TextField()
    estado = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    foto_problema = models.ImageField(upload_to='media/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    #request_id=models.CharField(max_length=100)
    #media_url = models.URLField(null=True, blank=True)
    #imagen = models.ImageField(upload_to='reportes/', null=True, blank=True) 


    class Meta:
        verbose_name='reporte'
        verbose_name_plural='reportes'

    def __str__(self):
        return f"Reporte de {self.usuario.username}: {self.descripcion_problema}"
    
class Servidor(AbstractUser):
    nombre_completo = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10)
    lugar_residencia = models.CharField(max_length=100)
    email = models.EmailField()
    groups = models.ManyToManyField(Group, related_name='servidores')
    user_permissions = models.ManyToManyField(Permission, related_name='servidores')

    def __str__(self):
        return self.username