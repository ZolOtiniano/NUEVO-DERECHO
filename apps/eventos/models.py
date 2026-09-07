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
    titulo = models.CharField(max_length=250, verbose_name="Título")
    subtitulo = models.CharField(max_length=500, blank=True, verbose_name="Subtítulo")
    tipo = models.CharField(max_length=30, choices=TIPOS, verbose_name="Tipo de evento")
    fecha_inicio = models.DateField(verbose_name="Fecha")
    fecha_fin = models.DateField(blank=True, null=True, verbose_name="Fecha fin")
    imagen = models.ImageField(upload_to="eventos/", verbose_name="Imagen")

    # =====================================================
    # CONTENIDO PRINCIPAL
    # =====================================================
    descripcion = models.TextField(blank=True, verbose_name="Texto principal")
    objetivo = models.TextField(blank=True, verbose_name="Objetivo")
    participantes = models.TextField(blank=True, verbose_name="Participantes")
    inversion = models.CharField(max_length=250, blank=True, verbose_name="Inversión")
    modalidad = models.CharField(max_length=250, blank=True, verbose_name="Modalidad")
    peso_academico = models.CharField(max_length=250, blank=True, verbose_name="Peso académico")
    enlace_primera_edicion = models.URLField(blank=True, verbose_name="Enlace Primera Edición")
    enlace_segunda_edicion = models.URLField(blank=True, verbose_name="Enlace Segunda Edición")

    # =====================================================
    # SECCIONES
    # =====================================================
    metodologia = models.TextField(blank=True, verbose_name="Metodología")

    conferencias_magistrales = models.TextField(
        blank=True,
        verbose_name="Conferencias magistrales",
        help_text="Especialistas nacionales e internacionales abordarán los "
                "principales desafíos de la enseñanza del Derecho en la era digital."
    )

    mesas_tematicas = models.TextField(
        blank=True,
        verbose_name="Mesas temáticas",
        help_text="Espacios de diálogo organizados en cuatro ejes: currículo jurídico, "
                "innovación e inteligencia artificial, formación práctica y "
                "evaluación por competencias."
    )

    call_for_papers = models.TextField(
        blank=True,
        verbose_name="Call for Papers",
        help_text="Presentación de investigaciones, experiencias docentes y propuestas "
                "de innovación pedagógica, seleccionadas mediante evaluación "
                "académica por pares."
    )

    exposicion_publicacion = models.TextField(
        blank=True,
        verbose_name="Exposición y publicación",
        help_text="Los trabajos seleccionados se presentarán en mesas temáticas del "
                "Congreso y podrán ser convocados al proceso editorial posterior."
    )

    programa = models.TextField(blank=True, verbose_name="Programa")

    cronograma = models.TextField(
        blank=True,
        verbose_name="Cronograma (obsoleto)",
        help_text="Campo en desuso, reemplazado por CronogramaItem."
    )

    organiza = models.TextField(blank=True, verbose_name="Organiza")
    auspician = models.TextField(blank=True, verbose_name="Auspician")


    contacto = models.TextField(blank=True, verbose_name="Comunícate con nosotros")
    correo_contacto = models.EmailField(blank=True, verbose_name="Correo de contacto")
    telefono_contacto = models.CharField(max_length=100, blank=True, verbose_name="Teléfono de contacto")
    horario_atencion = models.CharField(max_length=100, blank=True, verbose_name="Horario de atención")


    # =====================================================
    # OTROS
    # =====================================================
    enlace = models.URLField(blank=True, verbose_name="Enlace externo")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return self.titulo


# =====================================================
# CRONOGRAMA (tablas estructuradas)
# =====================================================
class CronogramaItem(models.Model):

    GRUPO_CALL_FOR_PAPERS = "cfp"
    GRUPO_INSCRIPCION = "inscripcion"
    GRUPO_CHOICES = [
        (GRUPO_CALL_FOR_PAPERS, "Cronograma del Call for Papers"),
        (GRUPO_INSCRIPCION, "Cronograma de inscripción de asistentes"),
    ]

    evento = models.ForeignKey(
        Evento,
        related_name="cronograma_items",
        on_delete=models.CASCADE,
        verbose_name="Evento"
    )

    grupo = models.CharField(
        max_length=20,
        choices=GRUPO_CHOICES,
        default=GRUPO_CALL_FOR_PAPERS,
        verbose_name="Grupo / Tabla"
    )

    actividad = models.CharField(
        max_length=255,
        verbose_name="Actividad"
    )

    fecha = models.CharField(
        max_length=255,
        verbose_name="Fecha",
        help_text="Texto libre, admite rangos como 'Del 1 al 14 de octubre de 2026'."
    )

    orden = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Define el orden de aparición dentro de su tabla."
    )

    class Meta:
        ordering = ["evento", "grupo", "orden"]
        verbose_name = "Ítem de cronograma"
        verbose_name_plural = "Ítems de cronograma"

    def __str__(self):
        return f"{self.get_grupo_display()} — {self.actividad}"