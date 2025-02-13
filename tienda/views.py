from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Iniciar sesión automáticamente después de registrarse
            return redirect('ver_carrito')  # Redirigir al carrito o a otra página
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})
