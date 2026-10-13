from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # ADMIN
    path(
        "admin/backup/",
        include("apps.backup.urls")
    ),

    path(
        "admin/",
        admin.site.urls
    ),

    # HOME
    path(
        "",
        include("apps.home.urls")
    ),

    # EVENTOS
    path(
        "eventos/",
        include("apps.eventos.urls")
    ),

    # PÁGINAS
    path(
        "",
        include("apps.paginas.urls")
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )