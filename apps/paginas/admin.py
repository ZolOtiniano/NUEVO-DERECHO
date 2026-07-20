from django.contrib import admin

from .models import (
    Pagina,
    Hero,
    EncabezadoSeccion,
    Historia,
    Objetivo,
    Mision,
    Vision,
    PerfilEgresado,
    Valor,
    Autoridad,
    Funcion,
    Galeria,
    Documento,
    Noticia,
    Contacto,
    Persona,
)


# ==========================
# INLINES (Encabezados)
# ==========================

class EncabezadoSeccionInline(admin.TabularInline):

    model = EncabezadoSeccion

    extra = 1


# ==========================
# INLINES (OneToOne)
# ==========================

class HeroInline(admin.StackedInline):
    model = Hero
    extra = 0
    max_num = 1


class HistoriaInline(admin.StackedInline):
    model = Historia
    extra = 0
    max_num = 1


class ObjetivoInline(admin.TabularInline):
    model = Objetivo
    extra = 1


class MisionInline(admin.StackedInline):
    model = Mision
    extra = 0
    max_num = 1


class VisionInline(admin.StackedInline):
    model = Vision
    extra = 0
    max_num = 1


class ValorInline(admin.TabularInline):
    model = Valor
    extra = 1


class PerfilEgresadoInline(admin.StackedInline):
    model = PerfilEgresado
    extra = 1


class ContactoInline(admin.StackedInline):
    model = Contacto
    extra = 0
    max_num = 1


# ==========================
# INLINES (OneToMany)
# ==========================

class AutoridadInline(admin.TabularInline):
    model = Autoridad
    extra = 0


class FuncionInline(admin.TabularInline):
    model = Funcion
    extra = 0


class PersonaInline(admin.TabularInline):
    model = Persona
    extra = 0


class GaleriaInline(admin.TabularInline):
    model = Galeria
    extra = 0


class DocumentoInline(admin.TabularInline):
    model = Documento
    extra = 0


class NoticiaInline(admin.TabularInline):
    model = Noticia
    extra = 0


# ==========================
# PAGINA
# ==========================

@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "slug",
        "activo",
    )

    list_filter = (
        "activo",
    )

    search_fields = (
        "titulo",
    )

    prepopulated_fields = {
        "slug": ("titulo",)
    }

    inlines = [

         # Encabezados comunes
        EncabezadoSeccionInline,


        # 1. Hero
        HeroInline,

        # 2. Historia
        HistoriaInline,

        # 3. Objetivos
        ObjetivoInline,

        # 4. Misión
        MisionInline,

        # 5. Visión
        VisionInline,

        # 6. Valores
        ValorInline,

        # 7. Perfil del Egresado
        PerfilEgresadoInline,

        # 8. Autoridades
        AutoridadInline,

        # 9. Funciones
        FuncionInline,

        # 10. Personas
        PersonaInline,

        # 11. Galería
        GaleriaInline,

        # 12. Documentos
        DocumentoInline,

        # 13. Noticias
        NoticiaInline,

        # 14. Contacto
        ContactoInline,
    ]


    class Media:
        js = (
            "admin/js/collapsible_fieldsets.js",
        )