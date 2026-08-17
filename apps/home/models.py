from django.db import models
from apps.paginas.models import Pagina


class NavbarLogo(models.Model):
    logo = models.ImageField(
        upload_to="configuracion/",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Logo del Navbar"
        verbose_name_plural = "Logo del Navbar"

    def __str__(self):
        return "Logo del Navbar"


class NavbarMenu(models.Model):

    TIPO_MENU = (
        ("simple", "Menú Simple"),
        ("dropdown", "Menú con Submenú"),
    )

    nombre = models.CharField(max_length=100)

    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="menus"
    )

    url = models.CharField(
        max_length=200,
        blank=True,
        help_text="URL externa o personalizada"
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_MENU,
        default="simple"
    )

    padre = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="submenus"
    )

    orden = models.PositiveIntegerField(default=0)

    activo = models.BooleanField(default=True)


    class Meta:
        ordering = ["orden"]
        verbose_name = "Menú"
        verbose_name_plural = "Menús"


    def get_url(self):

        if self.pagina:
            return f"/{self.pagina.slug}/"

        if self.url:
            return self.url

        return "#"


    def __str__(self):

        if self.padre:
            return f"{self.padre.nombre} → {self.nombre}"

        return self.nombre



class Hero(models.Model):

    fondo = models.ImageField(
        upload_to="hero/"
    )

    titulo = models.CharField(
        max_length=200
    )

    subtitulo = models.TextField(
        blank=True
    )

    boton_texto = models.CharField(
        max_length=100,
        blank=True
    )

    boton_url = models.CharField(
        max_length=200,
        blank=True
    )

    orden = models.PositiveIntegerField(
        default=0
    )

    activo = models.BooleanField(
        default=True
    )


    class Meta:
        ordering = ["orden"]


    def __str__(self):
        return self.titulo
        
    






# from django.db import models


class Seccion(models.Model):

    class Nombre(models.TextChoices):
        CARACTERISTICAS = "caracteristicas", "Características"
        AUTORIDAD = "autoridad", "Autoridad"
        DOCUMENTOS = "documentos", "Documentos"
        NOTICIAS = "noticias", "Noticias"
        EVENTOS = "eventos", "Eventos"
        GALERIA = "galeria", "Galería"

    nombre = models.CharField(
        max_length=30,
        choices=Nombre.choices,
        unique=True,
        verbose_name="Sección"
    )

    subtitulo = models.CharField(
        max_length=150,
        blank=True
    )

    titulo = models.CharField(
        max_length=200
    )

    descripcion = models.TextField(
        blank=True
    )

    activo = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"

    def __str__(self):
        return self.get_nombre_display()
    
    





class Bienvenida(models.Model):
    subtitulo = models.CharField(
        max_length=100,
        default="Bienvenidos"
    )
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    mensaje = models.TextField(blank=True)

    class Meta:
        verbose_name = "Bienvenida"
        verbose_name_plural = "Bienvenidas"

    def __str__(self):
        return self.titulo
    




    
class Caracteristica(models.Model):
    icono = models.CharField(
        max_length=100,
        help_text="Ejemplo: bi bi-book-half"
    )

    titulo = models.CharField(max_length=150)

    descripcion = models.TextField()

    orden = models.PositiveIntegerField(default=0)

    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden"]
        verbose_name = "Característica"
        verbose_name_plural = "Características"

    def __str__(self):
        return self.titulo
    




class Autoridad(models.Model):
    nombre = models.CharField(max_length=200)

    cargo = models.CharField(max_length=150)

    foto = models.ImageField(
        upload_to="autoridades/"
    )

    gestion = models.CharField(
        max_length=50,
        help_text="Ejemplo: 2026 - 2030"
    )

    activo = models.BooleanField(default=True)

    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "Autoridad"
        verbose_name_plural = "Autoridades"

    def __str__(self):
        return f"{self.cargo} - {self.nombre}"




class Documento(models.Model):

    titulo = models.CharField(max_length=200)

    descripcion = models.TextField(blank=True)

    archivo = models.FileField(upload_to="documentos/")

    icono = models.CharField(
        max_length=100,
        default="bi bi-file-earmark-pdf"
    )

    orden = models.PositiveIntegerField(default=0)

    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden"]





class Noticia(models.Model):

    titulo = models.CharField(
        max_length=250
    )


    resumen = models.TextField(
        blank=True
    )


    contenido = models.TextField(
        blank=True
    )


    imagen = models.ImageField(
        upload_to="noticias/",
        blank=True,
        null=True
    )


    fecha = models.DateTimeField(
        auto_now_add=True
    )


    orden = models.PositiveIntegerField(
        default=0
    )


    activo = models.BooleanField(
        default=True
    )


    class Meta:

        ordering = ["orden"]

        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"



    def __str__(self):

        return self.titulo





class Evento(models.Model):

    titulo = models.CharField(
        max_length=250
    )


    descripcion = models.TextField()


    imagen = models.ImageField(
        upload_to="eventos/",
        blank=True,
        null=True
    )


    fecha = models.DateField()


    hora = models.TimeField(
        blank=True,
        null=True
    )


    lugar = models.CharField(
        max_length=200,
        blank=True
    )


    orden = models.PositiveIntegerField(
        default=0
    )


    activo = models.BooleanField(
        default=True
    )


    class Meta:

        ordering = ["fecha", "orden"]

        verbose_name = "Evento"
        verbose_name_plural = "Eventos"



    def __str__(self):

        return self.titulo






class Galeria(models.Model):


    CATEGORIAS = (

        ("academico", "Académico"),

        ("eventos", "Eventos"),

        ("ceremonias", "Ceremonias"),

        ("infraestructura", "Infraestructura"),

        ("estudiantes", "Estudiantes"),

        ("autoridades", "Autoridades"),

    )


    titulo = models.CharField(
        max_length=200
    )


    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        default="academico"
    )


    descripcion = models.TextField(
        blank=True
    )


    imagen = models.ImageField(
        upload_to="galeria/"
    )


    orden = models.PositiveIntegerField(
        default=0
    )


    activo = models.BooleanField(
        default=True
    )



    class Meta:

        ordering = [
            "orden"
        ]

        verbose_name = "Imagen de Galería"

        verbose_name_plural = "Galería"



    def __str__(self):

        return f"{self.titulo} - {self.get_categoria_display()}"