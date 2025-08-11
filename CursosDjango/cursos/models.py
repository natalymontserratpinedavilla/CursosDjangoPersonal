from django.db import models
from ckeditor.fields import RichTextField 

class Cursos(models.Model): #Define la estructura de nuestra tabla
    nombre = models.CharField(max_length=100,verbose_name = "Nombre")  # Nombre del curso
    descripcion = models.TextField(verbose_name = "Descripcción")
    precio = models.DecimalField(max_digits=8, decimal_places=2) #Texto largo
    duracion_horas = models.IntegerField(verbose_name = "Duración de horas")
    imagen = models.ImageField(null = True, upload_to="foto", verbose_name="Fotografía")  
    created = models.DateTimeField(auto_now_add=True ,verbose_name = "fecha de creación") #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True ,verbose_name = "fecha de editado")
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
    def __str__(self):
        return self.nombre
#Indica que se mostrára el nombre como valor en la tabla


class Actividad(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    actividad = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Curso")  # Corregido el nombre del campo
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment = RichTextField(verbose_name="Actividades")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]
    
    def __str__(self):
        return self.coment #indica que se mostrar el nombre como valor en la tabla

