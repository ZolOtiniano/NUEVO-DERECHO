from django.shortcuts import render, get_object_or_404
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


def detalle_evento(request, pk):
    evento = get_object_or_404(
        Evento,
        pk=pk,
        activo=True
    )

    return render(
        request,
        "eventos/detalle.html",
        {
            "evento": evento
        }
    )
