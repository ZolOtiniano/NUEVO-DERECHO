from django.contrib import admin

from .models import (
    NavbarLogo,
    NavbarMenu,
    Hero,
    Seccion,
    Bienvenida,
    Caracteristica,
    Galeria,
)



# =========================
# NAVBAR
# =========================

@admin.register(NavbarLogo)
class NavbarLogoAdmin(admin.ModelAdmin):
    pass



@admin.register(NavbarMenu)
class NavbarMenuAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "padre",
        "orden",
        "activo",
    )


    list_editable = (
        "orden",
        "activo",
    )


    fieldsets = (
        (
            "Información",
            {
                "fields": (
                    "nombre",
                    "pagina",
                    "url",
                    "tipo",
                    "padre",
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



# =========================
# HERO
# =========================
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "orden",
        "activo"
    )

    list_editable = (
        "orden",
        "activo"
    )



# =========================
# SECCIONES
# =========================

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "titulo",
        "activo",
    )

    list_editable = (
        "activo",
    )

    list_filter = (
        "activo",
    )

    fieldsets = (
        (
            "Contenido",
            {
                "fields": (
                    "nombre",
                    "subtitulo",
                    "titulo",
                    "descripcion",
                    "activo",
                )
            },
        ),
    )


# =========================
# BIENVENIDA
# =========================

@admin.register(Bienvenida)
class BienvenidaAdmin(admin.ModelAdmin):

    list_display = (
        "subtitulo",
        "titulo",
    )

    fieldsets = (
        (
            "Contenido",
            {
                "fields": (
                    "subtitulo",
                    "titulo",
                    "descripcion",
                    "mensaje",
                )
            },
        ),
    )






# =========================
# CARACTERÍSTICAS
# =========================
@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "orden",
        "activo",
    )


    list_editable = (
        "orden",
        "activo",
    )


    ordering = (
        "orden",
    )



# =========================
# AUTORIDAD / DECANO
# =========================





# =========================
# DOCUMENTOS ACADÉMICOS
# =========================



# =========================
# NOTICIAS
# =========================




# =========================
# EVENTOS
# =========================




# =========================
# GALERÍA
# =========================

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "categoria",
        "activo",
        "orden",
    )


    list_filter = (
        "categoria",
        "activo",
    )


    list_editable = (
        "activo",
        "orden",
    )


    ordering = (
        "orden",
    )