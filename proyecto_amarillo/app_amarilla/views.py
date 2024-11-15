from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.shortcuts import render, redirect

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificación simple de usuario y contraseña
        if username == 'admin' and password == 'contraseña':
            return redirect('cuarto')  # Redirige a la página principal si las credenciales son correctas
        elif username == 'usuario' and password == 'contraseña':
            return redirect('primero')  # Redirige a otro template si las credenciales son las de 'usuario2'
        else:
            error_message = 'Usuario o contraseña incorrectos'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')  # Muestra el formulario de login

def primero(request):
    return render(request, 'Primero.html')

def segundo(request):
    return render(request, 'Segundo.html')

def tercero(request):
    return render(request, 'Tercero.html')

def cuarto(request):
    return render(request, 'Cuarto.html')

def quinto(request):
    return render(request, 'Quinto.html')

def sexto(request):
    return render(request, 'Sexto.html')

def septimo(request):
    return render(request, 'Septimo.html')