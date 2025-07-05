from django.shortcuts import render

from .models import paciente
from .models import estudio
from .models import doctor 

from django.http import HttpResponse


def saludo(request):
    return HttpResponse("¡Hola, mundo!") 

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def nuevo_paciente(request,nombre):
    if nombre is not None:
       nuevo_paciente = paciente(
            nombre=nombre,
            apellido="Apellido",
            fecha_nacimiento="2000-01-01",
            email="apellido@gmail.com",
            obra_social="Obra Social Ejemplo"
    )
    
    nuevo_paciente.save()
    return render(request, 'mi_primer_app/nuevo_paciente.html', {'paciente': nuevo_paciente})   


def nuevo_estudio(request):
    return render(request , 'mi_primer_app/nuevo_estudio.html')
     
def nuevo_doctor(request,nombre):
    if nombre is not None:
        nuevo_doctor = doctor(
            nombre=nombre,
            apellido="Apellido",
            especialidad="Especialidad Ejemplo",
            email=""
        )
        nuevo_doctor.save()
        return render(request, 'mi_primer_app/nuevo_doctor.html', {'doctor': nuevo_doctor})