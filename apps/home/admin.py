from django.contrib import admin

from .models import (
    NavbarLogo,
    NavbarMenu,
    Hero,
    Seccion,
    Bienvenida,
    Caracteristica,
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

    def get_fields(self, request, obj=None):
        # Tanto al añadir como al editar, solo se muestra la imagen.
        return ["fondo"]



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
# Se eliminó de aquí porque ya existe como su propia sección
# dedicada ("Galería"), registrada en apps/galeria/admin.py.
# El modelo Galeria de este archivo (home/models.py) sigue
# existiendo pero ya no aparece en el admin.


# =========================
# ORDEN DE SECCIONES EN EL ADMIN
# =========================
# Django ordena las secciones alfabéticamente por defecto.
# Aquí definimos el orden que queremos ver en /admin/.
ORDEN_APPS = [
    "home",
    "autoridades",
    "documentos",
    "eventos",
    "noticias",
    "galeria",
    "paginas",
    "auth",
]

# Orden de los modelos DENTRO de cada app (por app_label).
# La clave de cada modelo es su nombre en minúsculas (object_name.lower()).
ORDEN_MODELOS = {
    "home": [
        "navbarlogo",
        "navbarmenu",
        "hero",
        "seccion",
        "bienvenida",
        "caracteristica",
    ],
}

_original_get_app_list = admin.AdminSite.get_app_list


def get_app_list(self, request, app_label=None):
    app_list = _original_get_app_list(self, request, app_label=app_label)

    def posicion_app(app):
        try:
            return ORDEN_APPS.index(app["app_label"])
        except ValueError:
            return len(ORDEN_APPS)

    app_list = sorted(app_list, key=posicion_app)

    for app in app_list:
        orden_modelos = ORDEN_MODELOS.get(app["app_label"])
        if not orden_modelos:
            continue

        def posicion_modelo(modelo, orden=orden_modelos):
            nombre = modelo["object_name"].lower()
            try:
                return orden.index(nombre)
            except ValueError:
                return len(orden)

        app["models"] = sorted(app["models"], key=posicion_modelo)

    return app_list


admin.AdminSite.get_app_list = get_app_list