from django.urls import path
from appfarmacia.views import *

urlpatterns = [
    path("", inicio),
    path("medicamentos/", medicamentos),
    path("medicos/", medicos),
    path("pacientes/", pacientes),
    path("proveedores/", proveedores)
    ]