from django.contrib import admin
from .models import Autoridad


@admin.register(Autoridad)
class AutoridadAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "cargo",
        "gestion",
        "orden",
        "activo",
    )

    list_filter = (
        "activo",
        "cargo",
    )

    search_fields = (
        "nombre",
        "cargo",
        "gestion",
        "descripcion",
    )

    ordering = (
        "orden",
        "id",
    )

    fieldsets = (
        (
            "Información de la autoridad",
            {
                "fields": (
                    "nombre",
                    "cargo",
                    "gestion",
                    "foto",
                    "descripcion",
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