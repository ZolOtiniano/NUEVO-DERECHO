from .models import (
    Hero,
    Seccion,
    Bienvenida,
    Caracteristica,
)

from django.shortcuts import render

from apps.autoridades.models import Autoridad
from apps.documentos.models import Documento
from apps.eventos.models import Evento
from apps.noticias.models import Noticia
from apps.galeria.models import Galeria

def index(request):

    # =====================================================
    # SECCIONES
    # =====================================================
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

    # =====================================================
    # CONTEXT
    # =====================================================
    context = {

        # -------------------------------------------------
        # HERO
        # -------------------------------------------------

        "heroes": Hero.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),

        # -------------------------------------------------
        # BIENVENIDA
        # -------------------------------------------------

        "bienvenida": Bienvenida.objects.first(),

        # -------------------------------------------------
        # SECCIONES
        # -------------------------------------------------

        "secciones": secciones,

        # -------------------------------------------------
        # CARACTERÍSTICAS
        # -------------------------------------------------

        "caracteristicas": Caracteristica.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),

        # -------------------------------------------------
        # AUTORIDADES
        # -------------------------------------------------

        "decano": Autoridad.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ).first(),

        # -------------------------------------------------
        # DOCUMENTOS
        # -------------------------------------------------

        "documentos": Documento.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),

        # -------------------------------------------------
        # EVENTOS
        # -------------------------------------------------

        "eventos": eventos,

        "eventos_grupos": eventos_grupos,

        # -------------------------------------------------
        # NOTICIAS
        # -------------------------------------------------

        "noticias": Noticia.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),

        # -------------------------------------------------
        # GALERÍA
        # -------------------------------------------------

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
        "autoridades/autoridades.html",
        {
            "autoridades": autoridades
        }
    )