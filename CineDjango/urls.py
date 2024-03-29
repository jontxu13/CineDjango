"""
Definition of urls for CineDjango.
"""
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             #"authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('voto/', views.voto, name='voto'),
    path('new_pelicula/', views.new_pelicula,name='new_pelicula'),
    path('generos/', views.generos,name='generos'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
