from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def contato(request):
    context = {
        'telefone': '(99) 99999-9999',
        'responsavel': 'Maria da Silva',
    }
    if request.method == 'POST':
        print(f"Nome: {request.POST['name']}")
        print(f"Email: {request.POST['email']}")
        print(f"Mensagem: {request.POST['message']}")
    return render(request, "contato.html", context)


def reserva(request):
    return render(request, "reserva.html")
