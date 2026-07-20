from django.db import models


class Pagina(models.Model):

    titulo = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    activo = models.BooleanField(default=True)


    def __str__(self):
        return self.titulo



# 1. HERO
class Hero(models.Model):

    pagina = models.OneToOneField(
        Pagina,
        on_delete=models.CASCADE,
        related_name="hero"
    )

    imagen = models.ImageField(
        upload_to="paginas/hero/"
    )


    def __str__(self):
        return f"Hero - {self.pagina}"





class EncabezadoSeccion(models.Model):

    class SeccionChoices(models.TextChoices):

        HISTORIA = "historia", "Historia"
        OBJETIVOS = "objetivos", "Objetivos"
        MISION = "mision", "Misión"
        VISION = "vision", "Visión"
        VALORES = "valores", "Valores"
        PERFIL = "perfiles_egresado", "Perfil del Egresado"
        AUTORIDADES = "autoridades", "Autoridades"
        FUNCIONES = "funciones", "Funciones"
        PERSONAS = "personas", "Personal"
        GALERIA = "galeria", "Galería"
        DOCUMENTOS = "documentos", "Documentos"
        NOTICIAS = "noticias", "Noticias"
        CONTACTO = "contacto", "Contacto"



    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="encabezados"
    )


    seccion = models.CharField(
        max_length=50,
        choices=SeccionChoices.choices
    )


    titulo = models.CharField(
        max_length=200
    )


    descripcion = models.TextField(
        blank=True
    )


    def __str__(self):
        return self.titulo
    


    

# 2. HISTORIA
class Historia(models.Model):

    pagina = models.OneToOneField(
        Pagina,
        on_delete=models.CASCADE,
        related_name="historia"
    )

    contenido = models.TextField()

    imagen = models.ImageField(
        upload_to="paginas/historia/",
        blank=True,
        null=True
    )


    def __str__(self):
        return "Historia - " + self.pagina.titulo






class Objetivo(models.Model):

    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="objetivos"
    )

    descripcion = models.CharField(max_length=300)

    orden = models.PositiveIntegerField(default=1)




# 3. MISIÓN
class Mision(models.Model):

    pagina = models.OneToOneField(
        Pagina,
        on_delete=models.CASCADE,
        related_name="mision"
    )

    titulo = models.CharField(max_length=200)

    descripcion = models.TextField()


    def __str__(self):
        return self.titulo



# 4. VISIÓN
class Vision(models.Model):

    pagina = models.OneToOneField(
        Pagina,
        on_delete=models.CASCADE,
        related_name="vision"
    )

    titulo = models.CharField(max_length=200)

    descripcion = models.TextField()


    def __str__(self):
        return self.titulo



# 5. VALORES
class Valor(models.Model):

    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="valores"
    )

    titulo = models.CharField(max_length=200)

    descripcion = models.TextField()

    orden = models.PositiveIntegerField(default=1)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo




class PerfilEgresado(models.Model):

    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="perfiles_egresado"
    )

    descripcion = models.TextField()

    orden = models.PositiveIntegerField(default=1)

    activo = models.BooleanField(default=True)


    class Meta:
        ordering = ["orden"]


    def __str__(self):
        return self.descripcion[:50]




# 6. AUTORIDADES
class Autoridad(models.Model):

    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="autoridades"
    )

    nombre = models.CharField(max_length=200)

    cargo = models.CharField(max_length=200)

    correo = models.EmailField(blank=True)

    foto = models.ImageField(
        upload_to="paginas/autoridades/"
    )

    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]






# 7. FUNCIONES
class Funcion(models.Model):
    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="funciones"
    )

    icono = models.CharField(
        max_length=100,
        blank=True,
        help_text="Ejemplo: bi-check2-circle"
    )

    funcion = models.CharField(
        max_length=300,
        verbose_name="Función"
    )

    orden = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["orden"]
        verbose_name = "Función"
        verbose_name_plural = "Funciones"

    def __str__(self):
        return self.funcion
    






# 8. PERSONAS
class Persona(models.Model):

    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="personas"
    )

    imagen = models.ImageField(
        upload_to="paginas/personas/"
    )

    nombre = models.CharField(
        max_length=200
    )

    correo = models.EmailField(
        blank=True
    )

    categoria = models.CharField(
        max_length=20,
    )

    orden = models.PositiveIntegerField(
        default=0
    )


    class Meta:
        ordering = ["orden"]


    def __str__(self):
        return self.nombre





# 9. GALERIA
class Galeria(models.Model):

    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="galerias"
    )

    imagen = models.ImageField(
        upload_to="paginas/galeria/"
    )

    def __str__(self):
        return self.pagina.titulo



# 10. DOCUMENTOS
class Documento(models.Model):

    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="documentos"
    )

    titulo = models.CharField(max_length=200)

    archivo = models.FileField(
        upload_to="paginas/documentos/"
    )


    def __str__(self):
        return self.titulo



# 11. NOTICIAS
class Noticia(models.Model):

    pagina = models.ForeignKey(
        Pagina,
        on_delete=models.CASCADE,
        related_name="noticias"
    )

    titulo = models.CharField(max_length=200)

    descripcion = models.TextField()

    imagen = models.ImageField(
        upload_to="paginas/noticias/"
    )


    def __str__(self):
        return self.titulo



# 12. CONTACTO
class Contacto(models.Model):

    pagina = models.OneToOneField(
        Pagina,
        on_delete=models.CASCADE,
        related_name="contacto"
    )

    direccion = models.CharField(
        max_length=300,
        blank=True
    )

    telefono = models.CharField(
        max_length=50,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )


    # Redes sociales
    facebook = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    youtube = models.URLField(
        blank=True
    )

    whatsapp = models.CharField(
        max_length=50,
        blank=True
    )


    def __str__(self):
        return f"Contacto - {self.pagina.titulo}"
    
