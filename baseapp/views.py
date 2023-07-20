from django.shortcuts import render
from django.http import HttpResponse


def pag_inicial(request):
    return render(request, 'index')


def contato_email(request):
    return render(request, "contato")


def reserva_pet(request):
    return render(request, "reserva")
