from django.shortcuts import render

# Create your views here.

from .models import Persona



#objects es un intermediador para hacer consulta en la bd
def inicio(request):
	personas = Persona.objects.all()
	contexto = {
	   'personas':personas
	}

	return render(request,"index.html",contexto)

	


def crearPersona(request):
	return render(request,'crear.html')