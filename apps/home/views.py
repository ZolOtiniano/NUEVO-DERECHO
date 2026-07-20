from django.shortcuts import render

from .models import (
    Hero,
    Seccion,
    Bienvenida,
    Caracteristica,
    Autoridad,
    Documento,
    Noticia,
    Evento,
    Galeria,
)



def index(request):


    secciones = {
        seccion.nombre: seccion
        for seccion in Seccion.objects.filter(activo=True)
    }


    context = {


        # Hero
        "heroes": Hero.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),



        # Bienvenida
        "bienvenida": Bienvenida.objects.first(),


        # Todas las secciones
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



        # Documentos académicos
        "documentos": Documento.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),



        # Noticias
        "noticias": Noticia.objects.filter(
            activo=True
        ).order_by(
            "orden"
        ),



        # Eventos
        "eventos": Evento.objects.filter(
            activo=True
        ).order_by(
            "-fecha"
        )[:3],



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