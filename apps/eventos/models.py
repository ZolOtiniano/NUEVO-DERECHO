from django.db import models


class Evento(models.Model):

    TIPOS = [
        ("congreso", "Congreso"),
        ("seminario", "Seminario"),
        ("conferencia", "Conferencia"),
        ("taller", "Taller"),
        ("curso", "Curso"),
        ("diplomado", "Diplomado"),
    ]


    # =====================================================
    # INFORMACIÓN PRINCIPAL
    # =====================================================
    titulo = models.CharField(
        max_length=250,
        verbose_name="Título"
    )

    subtitulo = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Subtítulo"
    )

    tipo = models.CharField(
        max_length=30,
        choices=TIPOS,
        verbose_name="Tipo de evento"
    )

    fecha_inicio = models.DateField(
        verbose_name="Fecha"
    )

    fecha_fin = models.DateField(
        blank=True,
        null=True,
        verbose_name="Fecha fin"
    )

    imagen = models.ImageField(
        upload_to="eventos/",
        verbose_name="Imagen"
    )


    # =====================================================
    # CONTENIDO PRINCIPAL
    # =====================================================
    descripcion = models.TextField(
        blank=True,
        verbose_name="Texto principal"
    )

    objetivo = models.TextField(
        blank=True,
        verbose_name="Objetivo"
    )

    participantes = models.TextField(
        blank=True,
        verbose_name="Participantes"
    )

    inversion = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Inversión"
    )

    modalidad = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Modalidad"
    )

    peso_academico = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Peso académico"
    )

    enlace_primera_edicion = models.URLField(
        blank=True,
        verbose_name="Enlace Primera Edición"
    )

    enlace_segunda_edicion = models.URLField(
        blank=True,
        verbose_name="Enlace Segunda Edición"
    )


    # =====================================================
    # SECCIONES
    # =====================================================
    metodologia = models.TextField(
        blank=True,
        verbose_name="Metodología"
    )

    ponencias_magistrales = models.TextField(
        blank=True,
        verbose_name="Ponencias magistrales"
    )

    mesas_trabajo = models.TextField(
        blank=True,
        verbose_name="Mesas de trabajo"
    )

    presentacion_ponencias = models.TextField(
        blank=True,
        verbose_name="Presentación de ponencias"
    )

    enlace_certificados = models.URLField(
        blank=True,
        verbose_name="Enlace para descargar certificados"
    )





    programa = models.TextField(
        blank=True,
        verbose_name="Programa"
    )

    cronograma = models.TextField(
        blank=True,
        verbose_name="Cronograma"
    )

    organiza = models.TextField(
        blank=True,
        verbose_name="Organiza"
    )

    auspician = models.TextField(
        blank=True,
        verbose_name="Auspician"
    )

    contacto = models.TextField(
        blank=True,
        verbose_name="Comunícate con nosotros"
    )


    # =====================================================
    # OTROS
    # =====================================================
    enlace = models.URLField(
        blank=True,
        verbose_name="Enlace externo"
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return self.titulo