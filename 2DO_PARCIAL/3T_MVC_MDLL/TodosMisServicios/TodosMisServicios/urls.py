from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from MisServicios import views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MisServicios.urls', namespace="MisServicios")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]