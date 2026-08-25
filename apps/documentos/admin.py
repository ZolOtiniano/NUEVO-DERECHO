from django.contrib import admin
from .models import Documento


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "orden",
        "activo",
    )

    list_filter = (
        "activo",
    )

    search_fields = (
        "titulo",
        "descripcion",
    )

    ordering = (
        "orden",
        "id",
    )

    fieldsets = (
        (
            "Información del documento",
            {
                "fields": (
                    "titulo",
                    "descripcion",
                    "icono",
                    "archivo",
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