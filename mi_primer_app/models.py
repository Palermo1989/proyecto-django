from django.db import models

# Create your models here.


class paciente(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    email = models.EmailField()
    obra_social = models.CharField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class estudio(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fecha_estudio = models.DateField()
    tipo_estudio = models.CharField()
    resultado = models.TextField()

    def __str__(self):
        return f"Estudio de {self.paciente.nombre} - {self.tipo_estudio}"
    
class doctor(models.Model):
        nombre = models.CharField()
        apellido = models.CharField()
        especialidad = models.CharField()
        email = models.EmailField()

        def __str__(self):
            return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"