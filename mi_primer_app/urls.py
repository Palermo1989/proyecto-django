from django.urls import path
from .views import saludo, saludo_con_template ,nuevo_paciente , nuevo_estudio, nuevo_doctor, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola mundo/', saludo),  
    path('hola-template/', saludo_con_template),
    path('nuevo_paciente/<str:nombre>/', nuevo_paciente),
    path('nuevo_estudio/tipo_estudio/', nuevo_estudio),
    path('nuevo_doctor/<str:nombre>/', nuevo_doctor),
       
    
    ]
