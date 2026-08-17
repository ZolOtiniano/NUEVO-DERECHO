from django.contrib import admin
from .models import Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):

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
        "descripcion",
    )

    ordering = (
        "-fecha_inicio",
    )