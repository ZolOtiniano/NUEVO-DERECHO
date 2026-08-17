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

    titulo = models.CharField(
        max_length=250,
        verbose_name="Título"
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

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )

    enlace = models.URLField(
        blank=True,
        verbose_name="Enlace"
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