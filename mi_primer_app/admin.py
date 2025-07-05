from django.contrib import admin

# Register your models here.
from .models import paciente, estudio, doctor

register_models = [paciente, estudio, doctor]

admin.site.register(register_models)