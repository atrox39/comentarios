from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Usuario: "+self.nombre+" "+self.apellido
class Publicacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) # Llave foranea al usuario creador de la publicacion
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return "Titulo: "+self.titulo
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Usuario: "+self.usuario.nombre+" "+self.usuario.apellido+" | Publicacion: "+self.publicacion.titulo