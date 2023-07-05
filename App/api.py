#En este archivo crearemos el ViewSet, que junto con los serializers nos permiten crear API's

#importamos el modelo pre_home
from .models import pre_home
#importamos viewsets y permissions
from rest_framework import viewsets, permissions
#importamos el modelo del serializer
from .serializers import pre_homeSerializers

#creamos el ViewSet del modelo pre_home, el cuál heredará lo que ponemos dentro del parámetro
class pre_homeViewSet (viewsets.ModelViewSet) :
    #ponemos las consultas que se podrán hacer
    
    #hacemos que el conjunto de datos contenga todos los datos de la tabla pre_home
    queryset = pre_home.objects.all()
    #ponemos en una lista quienes tendrán permisos (en este caso AllowAny significa que todos tendrán permiso)
    permission_classes = [permissions.AllowAny]
    #ponemos desde qué serializer convertirá los datos
    serializer_class = pre_homeSerializers
