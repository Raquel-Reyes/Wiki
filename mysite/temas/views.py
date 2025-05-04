import requests
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import TemaForm

FIREBASE_BASE_URL = 'https://wiki-11737-default-rtdb.firebaseio.com/temas' 

def home(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            data = {
                'titulo': form.cleaned_data['titulo'],
                'contenido': form.cleaned_data['contenido'],
                'autor': form.cleaned_data['autor'],
            }
            requests.post(f'{FIREBASE_BASE_URL}.json', json=data)
            return redirect('home')
    else:
        form = TemaForm()

    # Obtener todos los temas desde Firebase
    response = requests.get(f'{FIREBASE_BASE_URL}.json')
    data = response.json() or {}

    temas = []
    for key, value in data.items():
        temas.append({
            'id': key,
            'titulo': value.get('titulo'),
            'contenido': value.get('contenido'),
            'autor': value.get('autor'),
        })

    temas.reverse()  
    return render(request, 'home.html', {'form': form, 'temas': temas})


def detalle_tema(request, tema_id):
    response = requests.get(f'{FIREBASE_BASE_URL}/{tema_id}.json')
    tema = response.json()

    if not tema:
        raise Http404("Tema no encontrado")

    return render(request, 'detalle.html', {'tema': tema})
