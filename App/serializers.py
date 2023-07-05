#en este archivo crearemos los serializers, los cuales junto con el ViewSet creado en api.py nos permitirán crear API's

#importamos el módulo serializers
from rest_framework import serializers

import App

#importamos el modelo pre_home
from .models import pre_home

#DESDE ESTE ARCHIVO, DJANGO SABRÁ QUE RESPONDER CUANDO SE HAGA UNA PETICIÓN POST, GET, Put y Delete

#creamos la clase que nos permita convertir el modelo en datos que puedan ser consultados
class pre_homeSerializers (serializers.ModelSerializer) :
    class Meta :
        #en model ponemos el nombre de la app
        model = App
        #ahora ponemos los campos que serán consultados dentro de una tupla. Los mismos serán los que tenemos dentro de la clase pre_home en el archivo models.py. También podemos verlos en las migraciones de la app
        fields = ('user', 'club')



