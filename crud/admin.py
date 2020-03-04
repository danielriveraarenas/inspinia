from django.contrib import admin
from .models import Marcas, Modelos, Colores, Autos

admin.site.register(Marcas)
admin.site.register(Modelos)
admin.site.register(Colores)
admin.site.register(Autos)
