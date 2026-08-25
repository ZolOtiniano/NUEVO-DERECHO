from django.db import models
from django.utils.text import slugify


class Noticia(models.Model):

    titulo = models.CharField(
        max_length=250,
        verbose_name="Título"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        verbose_name="Slug"
    )

    resumen = models.TextField(
        blank=True,
        verbose_name="Resumen"
    )

    contenido = models.TextField(
        verbose_name="Contenido"
    )

    imagen = models.ImageField(
        upload_to="noticias/",
        blank=True,
        null=True,
        verbose_name="Imagen"
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    orden = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["orden", "-created_at"]
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.titulo)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo