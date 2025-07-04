from django.db import models


# Create your models here.


class paciente(models.Model):
    nombre_paciente = models.CharField()
    apellido = models.CharField()
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    email = models.EmailField()
    obra_social = models.CharField()

    def __str__(self):
        return f"{self.nombre_paciente} {self.apellido}"

class estudio(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fecha_estudio = models.DateField()
    tipo_estudio = models.CharField()
    resultado = models.TextField()

    def __str__(self):
        return f"Estudio de {self.paciente.nombre_paciente} - {self.tipo_estudio}"
    

class doctor(models.Model):
        nombre_doctor = models.CharField()
        apellido = models.CharField()
        especialidad = models.CharField()
        email = models.EmailField()

        def __str__(self):
            return f"Dr. {self.nombre_doctor} {self.apellido} - {self.especialidad}"