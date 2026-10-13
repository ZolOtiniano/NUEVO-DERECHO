from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import FileResponse
from django.shortcuts import render, redirect


from django.conf import settings
from pathlib import Path
from datetime import datetime


from .services import (
    create_backup,
    save_backup,
    restore_backup,
)


@staff_member_required
def backup_center(request):

    if not request.user.is_superuser:
        messages.error(
            request,
            "No tienes permisos."
        )
        return redirect("/admin/")


    engine = settings.DATABASES["default"]["ENGINE"]


    if "sqlite" in engine:

        database_engine = "SQLite"


    elif "postgresql" in engine:

        database_engine = "PostgreSQL"


    elif "mysql" in engine:

        database_engine = "MySQL"


    else:

        database_engine = "Base de datos"


    context = {

        "database_engine":
            database_engine,

        "media_exists":
            Path(settings.MEDIA_ROOT).exists(),

        "server_time":
            datetime.now(),

    }


    return render(
        request,
        "admin/backup/backup_center.html",
        context
    )


@staff_member_required
def download_backup(request):
    """
    Genera y descarga un backup completo.
    """

    if not request.user.is_superuser:
        messages.error(
            request,
            "No tienes permisos para realizar backups."
        )
        return redirect("/admin/")

    backup_file = None

    try:

        backup_file = create_backup()

        messages.success(
            request,
            "Backup generado correctamente."
        )

        return FileResponse(
            open(backup_file, "rb"),
            as_attachment=True,
            filename=backup_file.name,
        )

    except Exception as error:

        messages.error(
            request,
            f"No se pudo crear el backup: {error}"
        )

        return redirect(
            "backup:backup_center"
        )




@staff_member_required
def create_server_backup(request):

    if not request.user.is_superuser:

        messages.error(
            request,
            "No tienes permisos."
        )

        return redirect("/admin/")


    try:

        backup_file = save_backup()


        messages.success(
            request,
            f"Backup creado correctamente: {backup_file.name}"
        )


    except Exception as error:

        messages.error(
            request,
            f"Error creando backup: {error}"
        )


    return redirect(
        "backup:backup_center"
    )



@staff_member_required
def upload_backup(request):
    """
    Sube y restaura un backup.

    Antes de restaurar:
    1. Valida el ZIP.
    2. Crea un backup de seguridad.
    3. Restaura la base de datos.
    4. Restaura media/.
    """

    if not request.user.is_superuser:

        messages.error(
            request,
            "No tienes permisos para restaurar backups."
        )

        return redirect("/admin/")

    if request.method != "POST":

        return redirect(
            "backup:backup_center"
        )

    backup_file = request.FILES.get(
        "backup_file"
    )

    confirmation = request.POST.get(
        "confirmation",
        "",
    ).strip()

    # -------------------------------------------------
    # CONFIRMACIÓN
    # -------------------------------------------------

    if confirmation != "RESTAURAR":

        messages.error(
            request,
            "Debes escribir exactamente RESTAURAR para confirmar."
        )

        return redirect(
            "backup:backup_center"
        )

    # -------------------------------------------------
    # ARCHIVO
    # -------------------------------------------------

    if not backup_file:

        messages.error(
            request,
            "Selecciona un archivo ZIP."
        )

        return redirect(
            "backup:backup_center"
        )

    # -------------------------------------------------
    # RESTAURAR
    # -------------------------------------------------

    try:

        safety_backup = restore_backup(
            backup_file
        )

        messages.success(
            request,
            "El backup fue restaurado correctamente."
        )

        messages.info(
            request,
            f"Backup de seguridad creado antes de restaurar: "
            f"{safety_backup.name}"
        )

    except Exception as error:

        messages.error(
            request,
            f"No se pudo restaurar el backup: {error}"
        )

    return redirect(
        "backup:backup_center"
    )