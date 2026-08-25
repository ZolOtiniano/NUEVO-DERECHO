from django.db import models


class Autoridad(models.Model):

    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre completo"
    )

    cargo = models.CharField(
        max_length=200,
        verbose_name="Cargo"
    )

    gestion = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Gestión"
    )

    foto = models.ImageField(
        upload_to="autoridades/",
        blank=True,
        null=True,
        verbose_name="Fotografía"
    )

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
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
        verbose_name = "Autoridad"
        verbose_name_plural = "Autoridades"

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"