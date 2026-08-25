from django.contrib import admin
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "orden",
        "activo",
        "created_at",
    )

    list_filter = (
        "activo",
        "created_at",
    )

    search_fields = (
        "titulo",
        "resumen",
        "contenido",
    )

    ordering = (
        "orden",
        "-created_at",
    )

    prepopulated_fields = {
        "slug": ("titulo",)
    }

    fieldsets = (
        (
            "Información de la noticia",
            {
                "fields": (
                    "titulo",
                    "slug",
                    "resumen",
                    "contenido",
                    "imagen",
                )
            }
        ),
        (
            "Configuración",
            {
                "fields": (
                    "orden",
                    "activo",
                )
            }
        ),
    )