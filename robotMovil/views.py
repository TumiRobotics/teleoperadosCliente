from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    mensaje_info = ''
    conectado = '0'
    url_consulta = ''
    if request.method == 'POST':
        ip_robot = request.POST.get('ipRobot')
        url_consulta = f'http://{ip_robot}:6060/robotMovil/verificarConexion'
        print(url_consulta)
        try:
            info = requests.get(url=url_consulta,timeout=1)
            conectado = '1'
            url_consulta = f'http://{ip_robot}:6060/robotMovil/'
        except:
            print('no se obtuvo conexion')
            conectado = '0'
            url_consulta = ''
            mensaje_info = 'No se pudo conectar'
    return render(request,'robotMovil/index.html',{
        'mensaje':mensaje_info,
        'conectado':conectado,
        'url_conexion':url_consulta,
    })