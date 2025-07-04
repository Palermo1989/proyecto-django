from django.urls import path
from .views import saludo, saludo_con_template ,crear_paciente

urlpatterns = [
    path('hola mundo/', saludo),  
    path('hola-template/', saludo_con_template),
    path('crear-paciente/<str:nombre>/', crear_paciente,),
   
]
