from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_autos/', views.get_autos, name='get_autos'),
    path('ins_auto/', views.ins_auto, name='ins_auto'),
    path('get_marcas/', views.get_marcas, name='get_marcas'),
    path('get_modelos/', views.get_modelos, name='get_modelos'),
    path('get_colores/', views.get_colores, name='get_colores'),
    path('upd_auto/<int:auto_id>/', views.upd_auto, name='upd_auto'),
]
