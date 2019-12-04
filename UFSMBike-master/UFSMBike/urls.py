from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^bicicleta/', include('bicicleta.urls')),
	url(r'^area/', include('area.urls')),
	url(r'^usuario/', include('usuario.urls')),
    #autenticacao
	url(r'^$', auth_views.login, {'template_name':'login.html'}, name='login'),
	url(r'^logout/', auth_views.logout,{'next_page' : '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]
