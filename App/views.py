from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from .models import pre_home
from .forms import PreHomeForm

#importamos csrf_exempt para poder eximir las vistas que querramos que no tengan necesidad de ser protegidas por el token CSRF
from django.views.decorators.csrf import csrf_exempt


#se mostrará en la página de inicio
def pre_home_view(request):
    #eximimos a esta vista de la verificación CSRF, para asi evitar errores de verificación
    csrf_exempt
    if request.method == 'POST':
        form = PreHomeForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Redirigimos al usuario a la URL 'home'
            return redirect('home')
    else:
        form = PreHomeForm()

    return render(request, 'pre_home.html', {'form': form})




#función que mediante ingresar /encuestas el usuario podrá ver todas las respuestas del formulario pre_home
def encuestas (request) :
    respuestas = list(pre_home_view.objects.values())
    return JsonResponse(respuestas, safe=False)
#DEVOLVER UN RENDER MOSTRANDO ESA LISTA EN EL TEMPLATE CORRESPONDIENTE


#vista de la página a la que se redireccionará el usuario una vez complete el formulario pre_home
def home_view (request) :
    return render(request, 'home.html')


#vistas de Home
def clubes (request) :
    return render(request, 'clubes.html')

def records (request) :
    return render(request, 'records.html')

def afa (request) :
    return render(request, 'afa.html')

#vistas de cada equipo de la liga argentina
def argentinos (request) :
    return render(request, 'argentinos.html')

def arsenal (request) :
    return render(request, 'arsenal.html')

def tucuman (request) :
    return render(request, 'tucuman.html')

def banfield (request) :
    return render(request, 'banfield.html')

def barracas (request) :
    return render(request, 'barracas.html')

def belgrano (request) :
    return render(request, 'belgrano.html')

def boca (request) :
    return render(request, 'boca.html')

def centralcordoba (request) :
    return render(request, 'centralcordoba.html')

def colon (request) :
    return render(request, 'colon.html')

def defensa (request) :
    return render(request, 'defensa.html')

def estudiantes (request) :
    return render(request, 'estudiantes.html')

def gimnasia (request) :
    return render(request, 'gimnasia.html')

def godoycruz (request) :
    return render(request, 'godoycruz.html')

def huracan (request) :
    return render(request, 'huracan.html')

def independiente (request) :
    return render(request, 'independiente.html')

def instituto (request) :
    return render(request, 'instituto.html')

def lanus (request) :
    return render(request, 'lanus.html')

def newells (request) :
    return render(request, 'newells.html')

def platense (request) :
    return render(request, 'platense.html')

def racing (request) :
    return render(request, 'racing.html')

def river (request) :
    return render(request, 'river.html')

def rosario (request) :
    return render(request, 'rosario.html')

def sanlorenzo (request) :
    return render(request, 'sanlorenzo.html')

def sarmiento (request) :
    return render(request, 'sarmiento.html')

def talleres (request) :
    return render(request, 'talleres.html')

def tigre (request) :
    return render(request, 'tigre.html')

def union (request) :
    return render(request, 'union.html')

def velez (request) :
    return render(request, 'velez.html')
