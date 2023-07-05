from django.contrib import admin
from .models import pre_home

#los agregamos al panel de administrador de Django usando el módulo admin importado por defecto en este archivo
admin.site.register(pre_home)


