from django.db import models

#modelo pre_home
class pre_home (models.Model) :
    user = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    
    #función que nos permite ver en Django admin los nombres de los objetos de la clase pre-home
    def __str__(self):
        return self.user #devuelve los valores almacenados en la variable user

