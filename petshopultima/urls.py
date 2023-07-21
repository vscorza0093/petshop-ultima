from django.contrib import admin
from django.urls import path

from baseapp.views import index, contato, reserva

urlpatterns = [
    path('', index),
    path("contato/", contato),
    path("reserva/", reserva),
    path("admin/", admin.site.urls),
]
