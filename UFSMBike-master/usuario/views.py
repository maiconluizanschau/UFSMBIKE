from django.views.generic import CreateView, UpdateView, TemplateView
from .models import Usuario
from bicicleta.models import Bicicleta
from area.models import Area
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy


class Criar(SuccessMessageMixin, CreateView):
    model = Usuario
    fields = ['matricula', 'cpf', 'nome', 'endereco', 'tel', 'email',
              'senha']
    template_name = 'novo-usuario.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['senha'])
        usuario.save()

        return super(Criar, self).form_valid(form)


class Editar(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['nome', 'cpf', 'endereco', 'tel', 'email', 'senha']
    template_name = 'editar-usuario.html'
    success_url = '.'
    success_message = 'Dados editados com sucesso!'

class ControleMultas(LoginRequiredMixin, TemplateView):
    template_name = 'controle-multas.html'

@login_required
def index(request):
    bicicletasDisponiveis = Bicicleta.objects.filter(emAluguel=False,emManutencao=False).exclude(areaAtual_id__isnull=True).all()
    totalBicicletas = Bicicleta.objects.filter(emAluguel=False,emManutencao=False).exclude(areaAtual_id__isnull=True).count()  # usar .filter antes
    areas = Area.objects.all()
    return render(request, "usuarios.html", {'areas':areas, 'bicicletas': bicicletasDisponiveis, 'totalBicicletas': totalBicicletas})

@login_required
def quitarMulta(request,pk):
    user = Usuario.objects.get(matricula=pk)
    user.multaSaldo = 0
    user.save()
    return redirect(index)

@login_required
def alugar(request,bikeId):
    user = Usuario.objects.get(matricula=request.user.pk)
    b = Bicicleta.objects.get(id=bikeId)
    if b.emAluguel == False and b.emManutencao == False:
        b.emAluguel = True
        b.save()
        user.bicicletaAlugada = b
        user.save()

    return redirect(index)

@login_required
def devolver(request,bikeId):
    user = Usuario.objects.get(matricula=request.user.pk)
    b = Bicicleta.objects.get(id=bikeId)
    b.emAluguel = False
    b.save()
    user.bicicletaAlugada = None
    user.save()
    return redirect(index)

@login_required
def adicionarMulta(request):
    #usar forms facilita a verificacao
    if request.POST.get('matricula','') and request.POST.get('multa','') != None:
        user = Usuario.objects.get(matricula=request.POST['matricula'])
        user.multaSaldo = request.POST['multa']
        user.save()

    return redirect('controle-multas')
