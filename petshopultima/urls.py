from django.contrib import admin
from django.urls import path

from baseapp.views import pag_inicial
from baseapp.views import contato_email
from baseapp.views import reserva_pet


urlpatterns = [
    path('', pag_inicial),
    path("contato/", contato_email),
    path("reserva/", reserva_pet),
    path("admin/", admin.site.urls),
]
