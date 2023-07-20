from django.shortcuts import render
from django.http import HttpResponse


def pag_inicial(request):
    return render(request, 'index.html')


def contato_email(request):
    return render(request, "contato.html")


def reserva_pet(request):
    return render(request, "reserva.html")
