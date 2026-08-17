from django.shortcuts import render
from .models import Evento


def eventos(request):
    eventos = Evento.objects.filter(
        activo=True
    ).order_by("-fecha_inicio")

    return render(
        request,
        "eventos/index.html",
        {
            "eventos": eventos
        }
    )