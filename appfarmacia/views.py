from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "appfarnacia/inicio.html")

def medicamentos(request):
    return render(request, "appfarmacia/medicamentos.html")

def medicos(request):
    return render(request, "appfarmacia/medicos.html")


def pacientes(request):
    return render(request, "appfarmacia/pacientes.html")

def proveedores(request):
    return render(request, "appfarmacia/proveedores.html")