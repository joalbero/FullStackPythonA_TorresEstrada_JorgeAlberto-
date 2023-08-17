from django.urls import path
from gestionamiento_app import views
from .views import BaseView
from gestionamiento_app.views import iniciar_sesion, ver_reportes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('contacto', views.contacto, name="Contacto"),
    path('registro/', views.registro_usuario, name='Registro'),
    path('login/', iniciar_sesion, name='Login'),
    path('logout/', views.cerrar_sesion, name='Logout'),
    path('crear_reporte/', views.crear_reporte, name='Crear_reporte'),
    path('ver_reportes/', views.ver_reportes, name='ver_reportes'),
    path('actualizar_status_reporte/<int:reporte_id>/', views.actualizar_status_reporte, name='actualizar_status_reporte'),
    path('', BaseView.as_view(), name='base'),
    path('reportes/', views.ListaReportes.as_view(), name='reportes'),
    path('api/reporte/list/', views.ReporteListAPIView.as_view(),),
]

#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)