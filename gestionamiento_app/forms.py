from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Reporte   

class RegistroForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nombre_completo', 'edad', 'sexo', 'lugar_residencia', 'email', 'contraseña')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ReporteForm(forms.ModelForm):
    #status = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    status = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    
    class Meta:
        model = Reporte
        fields = ('descripcion_problema', 'estado', 'municipio', 'direccion', 'foto_problema', 'status')
        widgets = {
            'descripcion_problema':forms.Textarea(attrs={'class':'form-control'}),
            #'status': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            #'estado':forms.TextInput(attrs={'class':'form-control'}),
        }