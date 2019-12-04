from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
	url(r'^novo/$', Criar.as_view(), name='novo-usuario'),
	url(r'^editar/(?P<pk>[\w-]+)/$', Editar.as_view(), name='editar-usuario'),
	url(r'^quitar/(?P<pk>[\w-]+)/$', quitarMulta, name='quitar-multa'),
	#bicicleta
	url(r'^alugar/(?P<bikeId>\d+)/$', alugar, name='alugar-bicicleta'),
	url(r'^devolver/(?P<bikeId>\d+)/$', devolver, name='devolver-bicicleta'),
	#controle
	url(r'^multa/', staff_member_required(ControleMultas.as_view()), name='controle-multas'),
	url(r'^adicionar/', adicionarMulta, name='adicionar-multa'),
	#index
	url(r'^$', index, name='index'),
]