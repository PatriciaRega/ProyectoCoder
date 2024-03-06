from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Medico, Solicitud, Paciente

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")   

def ver_medicos(request):
    return render(request, "ver_medicos.html")   

def ver_pacientes(request):
    return render(request, "ver_pacientes.html")   

def ver_solicitudes(request):
    return render(request, "ver_solicitudes.html")    



def crear_solicitud(request):

    solicitud_1 = Solicitud(farmaco="Ibuprofeno", fecha="2024-3-6", paciente = "Juana Perez", medico = "Luis Sosa")

    solicitud_1.save()

    info_solicitud = {"farmaco1": solicitud_1.farmaco}

    return render(request, "crear_solicitudes.html", info_solicitud)

#    return HttpResponse(f"{solicitud_1.medico}, la solicitud de dosificación de {solicitud_1.farmaco} para el paciente {solicitud_1.paciente} ha sido ingresada el dia {solicitud_1.fecha}")

def crear_paciente(request):

    paciente_1 = Paciente(nombre="Juana", apellido="Perez", edad = 22 , num_paciente = 1234)

    paciente_1.save()

    info_paciente = {"nombre1": paciente_1.nombre}

    return render(request, "crear_pacientes.html", info_paciente)

def crear_medico(request):

    medico_1 = Medico(nombre="Luis", apellido = "Sosa", email = "lsosa@hospital.com", num_registro=5015)

    medico_1.save()

    info_medico = {"nombre1":  medico_1.nombre}

    return render(request, "crear_medicos.html", info_medico)

