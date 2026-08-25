from django.contrib import admin
from .models import Galeria


@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "categoria",
        "orden",
        "activo",
    )

    list_filter = (
        "categoria",
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
            "Información de la imagen",
            {
                "fields": (
                    "titulo",
                    "descripcion",
                    "imagen",
                    "categoria",
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