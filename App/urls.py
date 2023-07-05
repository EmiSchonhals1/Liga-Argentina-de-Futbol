#en cada app creamos este archivo e importamos el módulo path
from django.urls import include, path
#además importamos las funciones que usará cada app
from . import views
from .views import afa, argentinos, arsenal, banfield, barracas, belgrano, boca, centralcordoba, clubes, colon, defensa, estudiantes, gimnasia, godoycruz, huracan, independiente, instituto, lanus, newells, platense, pre_home_view, racing, records, river, rosario, sanlorenzo, sarmiento, talleres, tigre, tucuman, union, velez

#Ahora crearemos las rutas de la API de forma sencilla usando el módulo routers de Django REST framework

#importamos el módulo routers
from rest_framework import routers
#importamos el ViewSet del modelo Project
from .api import pre_homeViewSet

#la variable router toma el valor de DefaultRouter(), el cual crea el CRUD
router = routers.DefaultRouter()

#registraremos en primer lugar el nombre de la ruta y luego el nombre del ViewSet (podemos agregarle como en este caso el nombre de esta ruta)
router.register('api/', pre_homeViewSet, 'api')

#urlpatterns tomará todas las urls generadas por router
urlpatterns = router.urls


urlpatterns = [
    path('', views.pre_home_view, name='pre_home'),
    path('encuestas/', views.encuestas),
    path('home/', views.home_view, name='home'),
    
    #
    path('clubes/', clubes, name = "clubes"),
    path('records/', records, name = "records"),
    path('afa/', afa, name = "afa"),
    
    #equipos de la liga
    path('argentinos/', argentinos, name = "argentinos"),
    path('arsenal/', arsenal, name = "arsenal"),
    path('tucuman/', tucuman, name = "tucuman"),
    path('banfield/', banfield, name = "banfield"),
    path('barracas/', barracas, name = "barracas"),
    path('belgrano/', belgrano, name = "belgrano"),
    path('boca/', boca, name = "boca"),
    path('centralcordoba/', centralcordoba, name = "centralcordoba"),
    path('colon/', colon, name = "colon"),
    path('defensa/', defensa, name = "defensa"),
    path('estudiantes/', estudiantes, name = "estudiantes"),
    path('gimnasia/', gimnasia, name = "gimnasia"),
    path('godoycruz/', godoycruz, name = "godoycruz"),
    path('huracan/', huracan, name = "huracan"),
    path('independiente/', independiente, name = "independiente"),
    path('instituto/', instituto, name = "instituto"),
    path('lanus/', lanus, name = "lanus"),
    path('newells/', newells, name = "newells"),
    path('platense/', platense, name = "platense"),
    path('racing/', racing, name = "racing"),
    path('river/', river, name = "river"),
    path('rosario/', rosario, name = "rosario"),
    path('sanlorenzo/', sanlorenzo, name = "sanlorenzo"),
    path('sarmiento/', sarmiento, name = "sarmiento"),
    path('talleres/', talleres, name = "talleres"),
    path('tigre/', tigre, name = "tigre"),
    path('union/', union, name = "union"),
    path('velez/', velez, name = "velez"),
]











