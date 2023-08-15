from django.shortcuts import render
from baseapp.forms import ContactForm
from baseapp.forms import PetShowerForm
import requests


def index(request):
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    data = response.json()

    i = 30
    dog_race = ""
    for letter in data['message']:
        if data['message'][i] != '/':
            dog_race += data['message'][i]
            i += 1
        else:
            break

    context = {
        'dog': data['message'],
        'race': dog_race
    }
    return render(request, 'index.html', context)


def contato(request):
    success = False
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            success = True
    context = {
        'telefone': '(99) 99999-9999',
        'responsavel': 'Maria da Silva',
        'form': form,
        'success': success
    }
    return render(request, "contato.html", context)


def reserva(request):
    if request.method == 'GET':
        form = PetShowerForm()
    else:
        form = PetShowerForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, "reserva.html", context)
