from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context 

def saludo(request):
    return HttpResponse('Hola Django - Coder')

def segundaVista(request):
    return HttpResponse('-----Ya somos programadores web----')

def dia(request):

    variable = datetime.now()

    return HttpResponse(variable)

def apellido(request, ape):


    fecha = datetime.now()
    return HttpResponse(f' El profe de coder {ape} es muy bueno..<br><br>.. Por lo menos hoy {fecha} ')

def probandoTemplate(request):

    miHTML = open('C:/Users/v-natalioti/Desktop/proyecto/Proyecto1/Proyecto1/plantillas/template1.html')

    plantilla = Template(miHTML.read())

    miHTML.close()

    miContexto = Context() 

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
    