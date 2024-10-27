"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cooperators.urls'), name='cooperators_list'),
    path('', include('assisteds.urls'), name='assisteds_list'),
    path('', include('responsibles.urls'), name='assisteds_list'),
    path('', include('requireds.urls'), name='requireds_list'),
    path('', include('processes.urls'), name='processes_list'),
    path('', include('home.urls'), name='home_list'),
    path('', include('agendas.urls'), name='agendas_list'),
    path('', include('notes.urls'), name='notes_list'),
    path('', include('subs.urls'), name='subs_list'),
    path('', include('accounts.urls'), name='accounts_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
