from django.db import models


class Galeria(models.Model):

    CATEGORIAS = (
        ("academico", "Académico"),
        ("eventos", "Eventos"),
        ("ceremonias", "Ceremonias"),
        ("infraestructura", "Infraestructura"),
    )

    titulo = models.CharField(
        max_length=200,
        verbose_name="Título"
    )

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )

    imagen = models.ImageField(
        upload_to="galeria/",
        verbose_name="Imagen"
    )

    categoria = models.CharField(
        max_length=30,
        choices=CATEGORIAS,
        default="academico",
        verbose_name="Categoría"
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
        verbose_name = "Foto de galería"
        verbose_name_plural = "Galería"

    def __str__(self):
        return self.titulo