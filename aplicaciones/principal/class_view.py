from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView #view
from django.urls import reverse_lazy
from .form import PersonaForm
from .models import Persona


class PersonaList(ListView):
	model=Persona
	template_name='index.html'
	# def get_queryset(self):
	# 	return self.model.objects.all()[:2]


class PersonaCreate(CreateView):
	"""docstring for PersonaCreate"""
	model=Persona
	form_class=PersonaForm
	template_name='crear.html'
	success_url=reverse_lazy('index')
	


class PersonaEditar(UpdateView):
	model=Persona
	form_class=PersonaForm
	template_name='crear.html'
	success_url=reverse_lazy('index')


class PersonaDelete(DeleteView):
	model=Persona
	template_name="verificacion.html"
	success_url=reverse_lazy('index')

		









"""
class View():
	dispatch:         verifica el metodo de la solicitud http
	http_not_allowed: 

	def get_queryset(self):
		return self.model.objects.all()

	def get_templates_names():
		return self.template_name

	def get(self,request,*args,**kwargs):
		return render(request,self_templates_names(),self.get_queryset())




class ListView(View):
	model         =Persona
	template_name=='index.html'

	def dispatch()

	def get_contex_data(self):
		context={}
		context['queryset']=self.get_queryset()
		return context

	def get_queryset(self):
		return self.model.objects.all()

	def get_templates_names():
		return self.template_name

	def get(self,request,*args,**kwargs):
		return render(request,self_templates_names(),self.get_queryset())
"""
