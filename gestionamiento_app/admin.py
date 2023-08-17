from django.contrib import admin
from .models import Reporte
#Register your models here.
class ReporteAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Reporte,ReporteAdmin)
