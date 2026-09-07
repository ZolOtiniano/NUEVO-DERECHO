from django.contrib import admin

from .models import Evento, CronogramaItem


class CronogramaItemInline(admin.TabularInline):
    model = CronogramaItem
    extra = 1
    fields = ("grupo", "actividad", "fecha", "orden")
    ordering = ("grupo", "orden")
    verbose_name = "Ítem de cronograma"
    verbose_name_plural = "Ítems de cronograma"


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
        "conferencias_magistrales",
        "mesas_tematicas",
        "call_for_papers",
        "exposicion_publicacion",
        "programa",
        "organiza",
        "auspician",
        "contacto",
    )

    ordering = (
        "-fecha_inicio",
    )

    inlines = (
        CronogramaItemInline,
    )


    # =====================================================
    # FORMULARIO
    # =====================================================

    fieldsets = (

        # -------------------------------------------------
        # 01 — HERO / INFORMACIÓN PRINCIPAL
        # -------------------------------------------------
        (
            "01 — Información principal",
            {
                "fields": (
                    "tipo",
                    "titulo",
                    "subtitulo",
                    "fecha_inicio",
                    "fecha_fin",
                )
            }
        ),

        # -------------------------------------------------
        # 02 — INTRODUCCIÓN
        # -------------------------------------------------
        (
            "02 — Introducción",
            {
                "fields": (
                    "imagen",
                    "descripcion",
                    "enlace_primera_edicion",
                    "enlace_segunda_edicion",
                )
            }
        ),

        # -------------------------------------------------
        # 03 — INFORMACIÓN DEL EVENTO
        # -------------------------------------------------
        (
            "03 — Información del evento",
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
        # 04 — METODOLOGÍA Y ACTIVIDADES
        # -------------------------------------------------
        (
            "04 — Metodología y actividades",
            {
                "fields": (
                    "metodologia",
                    "conferencias_magistrales",
                    "mesas_tematicas",
                    "call_for_papers",
                    "exposicion_publicacion",
                )
            }
        ),

        # -------------------------------------------------
        # 05 — PROGRAMA
        # -------------------------------------------------
        (
            "05 — Programa",
            {
                "fields": (
                    "programa",
                )
            }
        ),

        # -------------------------------------------------
        # 06 — CRONOGRAMA
        # -------------------------------------------------
        # El cronograma ahora se gestiona 100% desde el inline
        # de CronogramaItem (ver "inlines" arriba). El campo
        # "cronograma" (TextField) queda en desuso.

        # -------------------------------------------------
        # 07 — ORGANIZACIÓN
        # -------------------------------------------------
        (
            "07 — Organización",
            {
                "fields": (
                    "organiza",
                    "auspician",
                )
            }
        ),

        # -------------------------------------------------
        # 08 — CONTACTO
        # -------------------------------------------------
        (
            "08 — Contacto",
            {
                "fields": (
                    "contacto",
                    "correo_contacto",
                    "telefono_contacto",
                    "horario_atencion",
                    "enlace",
                )
            }
        ),
        # -------------------------------------------------
        # 09 — ESTADO
        # -------------------------------------------------
        (
            "09 — Estado",
            {
                "fields": (
                    "activo",
                )
            }
        ),

        # -------------------------------------------------
        # 10 — INFORMACIÓN DEL SISTEMA
        # -------------------------------------------------
        (
            "10 — Información del sistema",
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