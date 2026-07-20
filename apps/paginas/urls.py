from django.urls import path
from . import views

urlpatterns = [
    path(
        "<slug:slug>/",
        views.detalle_pagina,
        name="detalle_pagina"
    ),
]