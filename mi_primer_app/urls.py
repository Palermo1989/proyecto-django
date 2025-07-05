from django.urls import path
from .views import saludo, saludo_con_template ,nuevo_paciente , nuevo_estudio, nuevo_doctor

urlpatterns = [
    path('hola mundo/', saludo),  
    path('hola-template/', saludo_con_template),
    path('nuevo_paciente/<str:nombre>/', nuevo_paciente),
    path('nuevo_estudio/<str:tipo_estudio>/', nuevo_estudio),
    path('nuevo_doctor/<str:nombre>/', nuevo_doctor),
    
   
]
