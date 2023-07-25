from django.shortcuts import render
from baseapp.forms import ContactForm
from baseapp.forms import PetShowerForm


def index(request):
    return render(request, 'index.html')


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
