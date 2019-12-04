from django.conf.urls import url
from bicicleta.views import *

urlpatterns = [
	url(r'^nova/$', Criar.as_view(), name='nova-bicicleta'),
	url(r'^editar/(?P<pk>\d+)$', Editar.as_view(), name='editar-bicicleta'),
	url(r'^excluir/(?P<pk>\d+)$', Excluir.as_view(), name='excluir-bicicleta'),
	url(r'^conserto/(?P<bikeId>\d+)$', enviarConserto, name='controle-bicicleta'),
	url(r'^$', Lista.as_view(), name='lista-bicicleta'),
]