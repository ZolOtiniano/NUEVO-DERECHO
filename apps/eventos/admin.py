from django.contrib import admin
from .models import Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):

    # =====================================================
    # LISTADO
    # =====================================================

    list_display = (
        "titulo",
        "tipo",
        "fecha_inicio",
        "fecha_fin",
        "activo",
    )

    list_filter = (
        "tipo",
        "activo",
        "fecha_inicio",
    )

    search_fields = (
        "titulo",
        "subtitulo",
        "descripcion",
        "objetivo",
        "participantes",
        "inversion",
        "modalidad",
        "peso_academico",
        "metodologia",
        "ponencias_magistrales",
        "mesas_trabajo",
        "presentacion_ponencias",
        "programa",
        "cronograma",
        "organiza",
        "auspician",
        "contacto",
    )

    ordering = (
        "-fecha_inicio",
    )


    # =====================================================
    # FORMULARIO
    # =====================================================

    fieldsets = (

        # -------------------------------------------------
        # INFORMACIÓN PRINCIPAL
        # -------------------------------------------------

        (
            "Información principal",
            {
                "fields": (
                    "titulo",
                    "subtitulo",
                    "tipo",
                    "fecha_inicio",
                    "fecha_fin",
                    "imagen",
                )
            }
        ),


        # -------------------------------------------------
        # INFORMACIÓN ACADÉMICA
        # -------------------------------------------------

        (
            "Información académica",
            {
                "fields": (
                    "objetivo",
                    "participantes",
                    "inversion",
                    "modalidad",
                    "peso_academico",
                )
            }
        ),


        # -------------------------------------------------
        # CONTENIDO PRINCIPAL
        # -------------------------------------------------

        (
            "Contenido principal",
            {
                "fields": (
                    "descripcion",
                    "enlace_primera_edicion",
                    "enlace_segunda_edicion",
                )
            }
        ),


        # -------------------------------------------------
        # CONTENIDO DEL EVENTO
        # -------------------------------------------------

        (
            "Contenido del evento",
            {
                "fields": (
                    "metodologia",
                    "ponencias_magistrales",
                    "mesas_trabajo",
                    "presentacion_ponencias",
                    "programa",
                    "cronograma",
                )
            }
        ),



        (
            "Certificados",
            {
                "fields": (
                    "enlace_certificados",
                )
            }
        ),


        # -------------------------------------------------
        # ORGANIZACIÓN
        # -------------------------------------------------

        (
            "Organización",
            {
                "fields": (
                    "organiza",
                    "auspician",
                    "contacto",
                )
            }
        ),


        # -------------------------------------------------
        # ENLACES Y ESTADO
        # -------------------------------------------------

        (
            "Enlaces y estado",
            {
                "fields": (
                    "enlace",
                    "activo",
                )
            }
        ),


        # -------------------------------------------------
        # INFORMACIÓN DEL SISTEMA
        # -------------------------------------------------

        (
            "Información del sistema",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            }
        ),

    )


    # =====================================================
    # CAMPOS DE SOLO LECTURA
    # =====================================================

    readonly_fields = (
        "created_at",
        "updated_at",
    )