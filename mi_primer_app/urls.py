from django.urls import path
from .views import saludo, saludo_con_template ,crear_paciente, nuevo_estudio, nuevo_doctor

urlpatterns = [
    path('hola mundo/', saludo),  
    path('hola-template/', saludo_con_template),
    path('crear-paciente/<str:nombre>/', crear_paciente),
    path('nuevo-estudio/<str:nombre>/', nuevo_estudio),
    path('nuevo-doctor/<str:nombre>/', nuevo_doctor),
    
   
]
