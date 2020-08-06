from django.shortcuts import render,redirect

# Create your views here.

from .models import Persona
from .form import PersonaForm



#objects es un intermediador para hacer consulta en la bd
def inicio(request):
	personas = Persona.objects.all()
	contexto = {
	   'personas':personas
	}

	return render(request,"index.html",contexto)

	


def crearPersona(request):
	if request.method=="GET":
	     form =PersonaForm()
	     contexto ={
	         'form':form
	     }
	else:
		form = PersonaForm(request.POST)
		#print(form)
		if form.is_valid():
			form.save()
			return redirect('index')

	return render(request,'crear.html',{'form':form})



def editarPersona(request,id):
	persona = Persona.objects.get(id=id)
	if request.method == 'GET':
		form = PersonaForm(instance=persona)
		contexto={
		    'form':form
		}
	else:
		form=PersonaForm(request.POST,instance=persona)
		contexto={
		    'form':form
		}
		if form.is_valid():
			form.save()
	return render(request,'crear.html',contexto)
		



def eliminarPersona(request,id):
	persona=Persona.objects.get(id=id)
	persona.delete()
	return redirect('index')
