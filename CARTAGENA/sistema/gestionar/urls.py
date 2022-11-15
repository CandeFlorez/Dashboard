from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pobreza', views.pobreza, name='pobreza'),
    path('educacion', views.educacion, name='educacion'),
    path('empleo', views.empleo, name='empleo'),
    path('movilidad', views.movilidad, name='movilidad'),
    path('seguridad', views.seguridad, name='seguridad'),
]
