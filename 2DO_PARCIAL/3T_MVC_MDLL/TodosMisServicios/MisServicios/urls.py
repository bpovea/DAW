from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from MisServicios import views
from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
app_name="MisServicios"

urlpatterns = [
    path('lista/', views.lista),
    path('listaapi/', views.lista_api),
    re_path('usuariodetalles/(?P<id>\d+)$', views.servicios_prestados),

    re_path(r'usuarios/', views.usuarios.as_view()),    
    re_path(r'usuario/(?P<pk>[0-9]+)$', views.usuario_detalle.as_view()),
    re_path(r'usuario_servicio/(?P<pk>[0-9]+)$', views.usuario_servicio.as_view()),

    re_path(r'servicios/', views.servicios.as_view()),   
]
    
urlpatterns = format_suffix_patterns(urlpatterns)