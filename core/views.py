from django.shortcuts import render, redirect
from .models import Mascota, Slider, GL, Mision
from .forms import MascotaForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
# Create your views here.




def home(request):
    data = {
        'imagen':Slider.objects.all()
    }
    
    return render(request, 'core/home.html', data)


def galeria(request):
    data = {
        'foto':GL.objects.all()
    }
    
    return render(request, 'core/galeria.html', data)

def contacto(request):
    mision = Mision.objects.get(id=1)
    data = {
        'mision': mision
    }

    return render(request, 'core/contacto.html', data)

def formulario_cliente(request):
    return render(request, 'core/formulario_cliente.html')

def formulario_mascota(request):
    return render(request, 'core/formulario_mascota.html')

@permission_required('core.add_mascota')
def listado_mascota(request):
    mascotas = Mascota.objects.all()
    data = {
        'mascotas':mascotas
    }
    return render(request, 'core/listado_mascota.html', data)


def nueva_mascota(request):    
      data = {
          'form':MascotaForm()
      }  

      if request.method == 'POST':
          formulario = MascotaForm(request.POST, files=request.FILES)
          if formulario.is_valid():
              formulario.save()
              data['mensaje'] = "Guardado Correctamente"


      return render(request, 'core/nueva_mascota.html', data)


def modificar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    data = {
        'form': MascotaForm(instance=mascota)
    }
    
    if request.method == 'POST':
        formulario = MascotaForm(data=request.POST, instance=mascota, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data ['mensaje'] = "Modificado Correctamente"
            data ['form'] = MascotaForm(instance=Mascota.objects.get(id=id))
    return render(request, 'core/modificar_mascota.html', data)


def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    
    return redirect(to="listado_mascota")


def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == "POST":
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registrar.html', data)
    
