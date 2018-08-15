from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from MisServicios.models import *
import datetime
from django.shortcuts import render
from MisServicios.api_info.usuarios import *
from MisServicios.api_info.servicios import *
from MisServicios.api_info.usuarioServicios import *
from MisServicios.serializers import *
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate

def login(request):
    if request.user.is_authenticated:
        return render(request,'MisServicios/menu.html')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect("MisServicios:Menu")
            #return render(request,'MisServicios/menu.html')
        else:
            return render(request,'MisServicios/login.html',{'error':"formulario de inicio de sesión incorrecto"})
    else:
        return render(request,'MisServicios/login.html')
        

def menu(request):
    if request.COOKIES['pagina']:
        return redirect("MisServicios:"+request.COOKIES['pagina'])
        #return render(request,'MisServicios/'+request.COOKIES['pagina'] + '.html')
    else:
        return render(request,'MisServicios/menu.html')

def lista(request):
    usuarios = Usuario.objects.all()
    response = render(request,'MisServicios/lista.html',{'usuarios':usuarios})
    response.set_cookie('pagina',"lista")
    return response

def lista_api(request):
    if request.user.is_authenticated:
        response =  render(request,'MisServicios/listaapi.html')
        response.set_cookie('pagina',"listaapi")
        return response 

def servicios_prestados(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    return render(request,'MisServicios/serviciosPrestados.html',{"id":id,"usuario":usuario})

def registrarDatos():
    servicio1 = Servicio(nombre='Energia electrica',descripcion='descripcion energia electrica')
    servicio2 = Servicio(nombre='agua',descripcion='descripcion agua')
    servicio3 = Servicio(nombre='telefonia movil',descripcion='descripcion telefonia movil')
    servicio4 = Servicio(nombre='telefonia fija',descripcion='descripcion telefonia fija')
    
    servicio1.save()
    servicio2.save()
    servicio3.save()
    servicio4.save()

    usuario1 = Usuario(nombre = 'Mauricio', ciudad = 'Playas')
    usuario1.save()
    
    usuario2 = Usuario(nombre = 'David', ciudad = 'Playas')
    usuario2.save()

    usuario3 = Usuario(nombre = 'Byron', ciudad = 'Playas')
    usuario3.save()

    usuarioServicio1 = ServicioUsuario(usuario=usuario1,servicio=servicio1,fecha = datetime.datetime.strptime("2017-01-12","%Y-%m-%d"),direccion="guayaquil zona2",totalFactura =32.2) 
    usuarioServicio2 = ServicioUsuario(usuario=usuario2,servicio=servicio1,fecha = datetime.datetime.strptime("2017-01-12","%Y-%m-%d"),direccion="guayaquil zona2",totalFactura =32.2)
    usuarioServicio3 = ServicioUsuario(usuario=usuario3,servicio=servicio1,fecha = datetime.datetime.strptime("2018-01-12","%Y-%m-%d"),direccion="guayaquil zona3",totalFactura =32.2)
    usuarioServicio4 = ServicioUsuario(usuario=usuario1,servicio=servicio2,fecha = datetime.datetime.strptime("2019-01-12","%Y-%m-%d"),direccion="guayaquil zona3",totalFactura=32.2)
    usuarioServicio5 = ServicioUsuario(usuario=usuario2,servicio=servicio2,fecha = datetime.datetime.strptime("2017-01-12","%Y-%m-%d"),direccion="guayaquil zona2",totalFactura =32.2) 
    usuarioServicio6 = ServicioUsuario(usuario=usuario3,servicio=servicio2,fecha = datetime.datetime.strptime("2017-01-12","%Y-%m-%d"),direccion="guayaquil zona2",totalFactura=32.2)
    usuarioServicio7 = ServicioUsuario(usuario=usuario1,servicio=servicio3,fecha = datetime.datetime.strptime("2018-01-12","%Y-%m-%d"),direccion="guayaquil zona3",totalFactura =32.2)
    usuarioServicio8 = ServicioUsuario(usuario=usuario2,servicio=servicio3,fecha = datetime.datetime.strptime("2019-01-12","%Y-%m-%d"),direccion="guayaquil zona3",totalFactura=32.2)

    usuarioServicio1.save()
    usuarioServicio2.save()
    usuarioServicio3.save()
    usuarioServicio4.save()
    usuarioServicio5.save()
    usuarioServicio6.save()
    usuarioServicio7.save()
    usuarioServicio8.save()