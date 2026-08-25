from django.shortcuts import render
from .models import Documento


def documentos(request):

    documentos = Documento.objects.filter(
        activo=True
    )

    return render(
        request,
        "documentos/documentos.html",
        {
            "documentos": documentos,
        }
    )