#coding:utf-8
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from .models import Area
from bicicleta.models import Bicicleta

class Criar(SuccessMessageMixin, LoginRequiredMixin, CreateView):
	model = Area
	fields = ['nome','x','y']
	template_name = 'nova-area.html'
	success_url = reverse_lazy('lista-area')
	success_message = 'Área criado com sucesso.'

	def form_valid(self,form):
		area = form.save(commit=False)
		area.save()
		return super(Criar, self).form_valid(form)

class Editar(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = Area
	fields = ['nome','x','y']
	template_name = 'editar-area.html'
	success_url = reverse_lazy('lista-area')
	success_message = 'Área editado com sucesso.'

class Excluir(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
	model = Area
	template_name = 'excluir-area.html'
	success_url = reverse_lazy('lista-area')
	success_message = 'Área removido com sucesso.'

@login_required
def Lista(request):
	areas = Area.objects.all()
	bicicletas = Bicicleta.objects.all()

	return render(request,'areas.html',{'areas' : areas, 'bicicletas' : bicicletas})
