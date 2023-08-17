from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Home')
        
        else:
            return render(request,"registro/registro.html",{"form": form})
        
def cerrar_sesion(request):
    logout(request)

    return redirect('Home')

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contrasena)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                return render(request, "login/login.html", {"form": form})
        else:
            return render(request, "login/login.html", {"form": form})


    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})

