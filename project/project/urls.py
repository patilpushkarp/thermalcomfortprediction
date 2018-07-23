"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from myapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sig/', TemplateView.as_view(template_name = 'siup')),
    path('reg', views.register, name='register'),
    path('led/', views.led, name='led'),
    path('but1', views.control1, name='control1'),
    path('but0', views.control0, name='control0'),
    path('', views.formView, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('data/', views.thermal, name='data')
]
