from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Lista, Cancion
from django.views.generic import TemplateView, DetailView, ListView
from django.views import generic

# Create your views here.

class ListView(ListView):
	template_name = 'musica/listado.html'
	model = Lista
	fields = ['puesto', 'varpuesto', 'fechaent', 'semanas', 'nomcancion', 'autor']

	def get_queryset(self):
		self.lista = get_object_or_404(Lista, name=self.args[0])
		return Lista.objects.filter(nomcancion=self.nomcancion)

	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['cancion_list'] = Lista.objects.all()
		return context

def index(request):
	template = loader.get_template('polls/index.html')
	return HttpResponse(template.render(request))
