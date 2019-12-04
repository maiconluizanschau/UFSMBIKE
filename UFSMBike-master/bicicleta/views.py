#coding:utf-8
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from .models import Bicicleta

class Criar(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    model = Bicicleta
    fields = ['modelo', 'areaAtual']
    template_name = 'nova-bicicleta.html'
    success_url = '.'
    success_message = 'Bicicleta criada com sucesso'

    def form_valid(self, form):
        bicicleta = form.save(commit=False)
        bicicleta.save()
        return super(Criar, self).form_valid(form)
        

class Lista(SuccessMessageMixin, LoginRequiredMixin,ListView):
    model = Bicicleta
    context_object_name = 'bicicletas'
    template_name = 'bicicletas.html'

class Editar(SuccessMessageMixin, LoginRequiredMixin,UpdateView):
    model = Bicicleta
    fields = ['modelo','areaAtual']
    template_name = 'editar-bicicleta.html'
    success_url = reverse_lazy('lista-bicicleta')
    success_message = 'Bicicleta editada com sucesso'

class Excluir(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Bicicleta
    success_message = 'Bicicleta removida com sucesso.'
    template_name = 'excluir-bicicleta.html'
    success_url = reverse_lazy('lista-bicicleta')
    success_message = 'Bicicleta excluída com sucesso'

@login_required
def enviarConserto(request,bikeId):
    b = Bicicleta.objects.get(id=bikeId)
    if b.emManutencao:
        b.emManutencao = False
        messages.success(request,'Bicicleta '+str(b.id)+' retornada a frota.')
    else:
        b.emManutencao = True
        messages.success(request,'Bicicleta '+str(b.id)+' enviada para manutenção.')
    b.save()
    return redirect('lista-bicicleta')
