"""ProyectoCabros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('guitarra/', views.guitarra, name="guitarra"),
    path('bajos/', views.bajos, name="bajos"),
    path('piano/', views.piano, name="piano"),
    path('percusion/', views.percusion, name="percusion"),
    path('amplificador/', views.amplificador, name="amplificador"),

    path('personal/', views.personal, name="personal"),

    path('otrosAccesorios/', views.otrosAccesorios, name="otrosAccesorios"),


    path('inicioSesion/', views.inicioSesion, name="inicioSesion"),


    path('crearCuenta/', views.crearCuenta, name="crearCuenta"),

    path('inicioAdmin/', views.inicioAdmin, name="inicioAdmin"),
 
]
