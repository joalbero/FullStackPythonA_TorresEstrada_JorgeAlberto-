from rest_framework import serializers
from .models import Reporte

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = (
            'id',
            'status',
            'usuario',
            'descripcion_problema',
            'estado',
            'municipio',
            'direccion',    
        )
