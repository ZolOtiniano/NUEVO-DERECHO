from django.shortcuts import render, get_object_or_404

from .models import Pagina



def detalle_pagina(request, slug):

    pagina = get_object_or_404(

        Pagina.objects
        .select_related(
            "hero",
            "historia",
            "mision",
            "vision",
            "contacto",
        )
        .prefetch_related(

            "encabezados",

            "objetivos",

            "perfiles_egresado",

            "valores",

            "funciones",

            "galerias",

            "documentos",

            "noticias",


            # Autoridades
            "autoridades",


            # Personas
            "personas",

        ),

        slug=slug,

        activo=True

    )



    autoridades = pagina.autoridades.all()


    contexto = {

        "pagina": pagina,


        # Encabezados
        "encabezados": pagina.encabezados.all(),


        # Autoridades
        "autoridad_principal": autoridades.first(),

        "otras_autoridades": autoridades[1:],


        # Personas
        "personas": pagina.personas.all(),

    }



    return render(

        request,

        "paginas/detalle.html",

        contexto

    )