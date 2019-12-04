from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^nova/$', Criar.as_view(), name='nova-area'),
	url(r'^editar/(?P<pk>\d+)$', Editar.as_view(), name='editar-area'),
	url(r'^excluir/(?P<pk>\d+)$', Excluir.as_view(), name='excluir-area'),
	url(r'^$', Lista, name='lista-area'),
]