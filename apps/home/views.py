from django.shortcuts import render

from .models import (
    Hero,
    Seccion,
    Bienvenida,
    Caracteristica,
    Autoridad,
    Documento,
    Noticia,
    Galeria,
)

from apps.eventos.models import Evento


def index(request):

    secciones = {
        seccion.nombre: seccion
        for seccion in Seccion.objects.filter(activo=True)
    }

    # =====================================================
    # EVENTOS
    # =====================================================

    eventos = Evento.objects.filter(
        activo=True
    ).order_by(
        "-fecha_inicio"
    )

    eventos_grupos = [
        eventos[i:i + 3]
        for i in range(0, len(eventos), 3)
    ]


    context = {

        # Hero
        "heroes": Hero.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),

        # Bienvenida
        "bienvenida": Bienvenida.objects.first(),

        # Secciones
        "secciones": secciones,

        # Características
        "caracteristicas": Caracteristica.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),

        # Decano
        "decano": Autoridad.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ).first(),

        # Documentos
        "documentos": Documento.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),

        # Eventos
        "eventos": eventos,
        "eventos_grupos": eventos_grupos,

        # Noticias
        "noticias": Noticia.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),

        # Galería
        "galeria": Galeria.objects.filter(
            activo=True
        ).order_by(
            "orden"
        )[:8],
    }


    return render(
        request,
        "home/index.html",
        context
    )


def autoridades(request):

    autoridades = Autoridad.objects.filter(
        activo=True
    ).order_by(
        "orden"
    )

    return render(
        request,
        "home/autoridades.html",
        {
            "autoridades": autoridades
        }
    )