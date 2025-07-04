from django.urls import path
from .views import saludo, saludo_con_template, nuevo_paciente, nuevo_estudio, nuevo_doctor  

urlpatterns = [
    path('hola mundo/', saludo),  
    path('hola-template/', saludo_con_template),
    path('crear-paciente/<str:nombre>/', nuevo_paciente, name='crear_paciente'),
    path('crear-estudio/<str:nombre>/', nuevo_estudio, name='crear'),
    path('crear-doctor/<str:nombre>/', nuevo_doctor, name='crear_doctor')   
]
