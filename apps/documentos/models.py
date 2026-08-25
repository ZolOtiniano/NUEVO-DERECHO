from django.db import models


class Documento(models.Model):

    titulo = models.CharField(
        max_length=200,
        verbose_name="Título"
    )

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )

    icono = models.CharField(
        max_length=100,
        default="bi bi-file-earmark-text",
        verbose_name="Icono Bootstrap"
    )

    archivo = models.FileField(
        upload_to="documentos/",
        blank=True,
        null=True,
        verbose_name="Archivo"
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    orden = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden"
    )

    class Meta:
        ordering = ["orden", "id"]
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.titulo