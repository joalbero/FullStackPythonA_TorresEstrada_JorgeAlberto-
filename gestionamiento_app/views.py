from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from gestionamiento_app.models import Reporte
from gestionamiento_app.forms import ReporteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from .forms import RegistroForm, ReporteForm, LoginForm
from .models import Reporte
from django.http import HttpResponseBadRequest
from rest_framework.generics import ListAPIView
from django.views.generic.list import ListView
from .serializers import ReporteSerializer


class BaseView(TemplateView):
    template_name = 'gestionamiento_app/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega el contexto
        context['reporte'] = Reporte.objects.first()  # obtener el primer reporte de la base de datos
        return context

def home(request):
    return render(request, "gestionamiento_app/home.html")

def contacto(request):
    return render(request, "gestionamiento_app/contacto.html")                                  

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'gestionamiento_app/registro.html', {'form': form})
            

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'gestionamiento_app/login.html', {'form': form, 'error': 'Credenciales inválidas'})
    else:
        form = LoginForm()
    return render(request, 'gestionamiento_app/login.html', {'form': form})

def cerrar_sesion(request):
    return redirect('login')

@login_required
def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.usuario = request.user
            reporte.save()
            return redirect(reverse('ver_reportes'))
    else:
        form = ReporteForm()
    return render(request, 'gestionamiento_app/crear_reporte.html', {'form': form})

@login_required
def ver_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'gestionamiento_app/ver_reportes.html', {'reportes': reportes})

class ListaReportes(ListView):
    template_name = "gestionamiento_app/ver_reportes.html"
    context_object_name = 'Reportes'

    def get_queryset(self):
        return Reporte.objects.all()

class ReporteListAPIView(ListAPIView):

    serializer_class = ReporteSerializer

    def get_queryset(self):
        return Reporte.objects.all()


@login_required
def actualizar_status_reporte(request, reporte_id):
    reporte = get_object_or_404(Reporte, pk=reporte_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status:
            reporte.status = status
            reporte.save()
            return redirect('ver_reportes')  # Redirigir a la página de visualización de reportes
        else:
            return HttpResponseBadRequest("Campo 'status' faltante en la solicitud")
    else:
        url = reverse('ver_reportes')
        return render(request, 'gestionamiento_app/actualizar_status_reporte.html', {'reporte': reporte, 'url': url})
    




