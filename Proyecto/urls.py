
from django.contrib import admin
from django.urls import path, include
#importamos las urls de la app
import App.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #agregamos las urls de la app
    path('', include('App.urls')),
]
