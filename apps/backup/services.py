import json
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.core.management import call_command


BACKUP_PREFIX = "backup_"
BACKUP_STORAGE = Path(settings.BASE_DIR) / "backups"

# Carpeta para guardar backups de seguridad
# fuera de media/ para evitar backups dentro de backups.
BACKUP_STORAGE = Path(settings.BASE_DIR) / "backups"


def create_backup(destination=None):
    """
    Crea un ZIP con:

    - database.json
    - manifest.json
    - media/

    Si destination no se indica, el ZIP se crea temporalmente
    y se devuelve su ruta.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_name = f"{BACKUP_PREFIX}{timestamp}.zip"

    temp_dir = Path(
        tempfile.mkdtemp(
            prefix="django_backup_"
        )
    )

    try:

        # -------------------------------------------------
        # 1. EXPORTAR BASE DE DATOS
        # -------------------------------------------------

        database_file = temp_dir / "database.json"

        with open(
            database_file,
            "w",
            encoding="utf-8",
        ) as file:

            call_command(
                "dumpdata",
                "--natural-foreign",
                "--natural-primary",
                "--indent",
                "2",
                stdout=file,
            )

        # -------------------------------------------------
        # 2. COPIAR MEDIA
        # -------------------------------------------------

        media_source = Path(settings.MEDIA_ROOT)

        media_destination = temp_dir / "media"

        if media_source.exists():

            shutil.copytree(
                media_source,
                media_destination,
                dirs_exist_ok=True,
            )

        else:

            media_destination.mkdir(
                parents=True,
                exist_ok=True,
            )

        # -------------------------------------------------
        # 3. MANIFEST
        # -------------------------------------------------

        manifest = {
            "backup_version": "1.0",
            "created_at": datetime.now().isoformat(),
            "database": "django-dumpdata",
            "includes_media": True,
        }

        with open(
            temp_dir / "manifest.json",
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                manifest,
                file,
                indent=2,
                ensure_ascii=False,
            )

        # -------------------------------------------------
        # 4. UBICACIÓN DEL ZIP
        # -------------------------------------------------

        if destination:

            destination = Path(destination)

            destination.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            zip_path = destination

        else:

            zip_path = (
                Path(tempfile.gettempdir())
                / backup_name
            )

        # -------------------------------------------------
        # 5. CREAR ZIP
        # -------------------------------------------------

        with zipfile.ZipFile(
            zip_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
        ) as zip_file:

            for file_path in temp_dir.rglob("*"):

                if file_path.is_file():

                    relative_path = (
                        file_path.relative_to(temp_dir)
                    )

                    zip_file.write(
                        file_path,
                        relative_path,
                    )

        return zip_path

    finally:

        shutil.rmtree(
            temp_dir,
            ignore_errors=True,
        )


def validate_backup(backup_file):
    """
    Valida que el archivo sea un backup ZIP
    generado por este sistema.
    """

    if not backup_file:

        raise ValueError(
            "No se recibió ningún archivo."
        )

    if not backup_file.name.lower().endswith(".zip"):

        raise ValueError(
            "El backup debe estar en formato ZIP."
        )

    # Máximo 1 GB
    max_size = 1024 * 1024 * 1024

    if backup_file.size > max_size:

        raise ValueError(
            "El archivo de backup supera el límite permitido."
        )

    try:

        with zipfile.ZipFile(
            backup_file,
            "r",
        ) as zip_file:

            files = zip_file.namelist()

            # database.json obligatorio
            if "database.json" not in files:

                raise ValueError(
                    "El backup no contiene database.json."
                )

            # Validar rutas
            for member in zip_file.infolist():

                target_path = Path(
                    member.filename
                )

                # Ruta absoluta
                if target_path.is_absolute():

                    raise ValueError(
                        "El backup contiene una ruta no permitida."
                    )

                # ../
                if ".." in target_path.parts:

                    raise ValueError(
                        "El backup contiene una ruta peligrosa."
                    )

            # Verificar que database.json sea JSON válido
            database_content = zip_file.read(
                "database.json"
            )

            try:

                json.loads(
                    database_content.decode(
                        "utf-8"
                    )
                )

            except (UnicodeDecodeError, json.JSONDecodeError):

                raise ValueError(
                    "database.json no contiene un JSON válido."
                )

    except zipfile.BadZipFile:

        raise ValueError(
            "El archivo no es un ZIP válido."
        )

    return True


def create_safety_backup():
    """
    Crea un backup automático antes de restaurar.
    """

    BACKUP_STORAGE.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    backup_path = (
        BACKUP_STORAGE
        / f"pre_restore_{timestamp}.zip"
    )

    return create_backup(
        destination=backup_path
    )


def restore_backup(backup_file):
    """
    Restaura completamente:

    - Base de datos
    - media/

    Antes de restaurar crea automáticamente
    un backup de seguridad.
    """

    # -------------------------------------------------
    # 1. VALIDAR
    # -------------------------------------------------

    validate_backup(
        backup_file
    )

    # -------------------------------------------------
    # 2. BACKUP DE SEGURIDAD
    # -------------------------------------------------

    safety_backup = create_safety_backup()

    # -------------------------------------------------
    # 3. DIRECTORIO TEMPORAL
    # -------------------------------------------------

    temp_dir = Path(
        tempfile.mkdtemp(
            prefix="django_restore_"
        )
    )

    try:

        # -------------------------------------------------
        # 4. EXTRAER ZIP
        # -------------------------------------------------

        with zipfile.ZipFile(
            backup_file,
            "r",
        ) as zip_file:

            zip_file.extractall(
                temp_dir
            )

        database_file = (
            temp_dir / "database.json"
        )

        if not database_file.exists():

            raise ValueError(
                "No existe database.json en el backup."
            )

        # -------------------------------------------------
        # 5. RESTAURAR BASE DE DATOS
        # -------------------------------------------------

        # Vaciar la base de datos actual
        call_command(
            "flush",
            "--no-input",
        )

        # Cargar los datos del backup
        call_command(
            "loaddata",
            str(database_file),
        )

        # -------------------------------------------------
        # 6. RESTAURAR MEDIA
        # -------------------------------------------------

        media_backup = (
            temp_dir / "media"
        )

        media_destination = Path(
            settings.MEDIA_ROOT
        )

        if media_backup.exists():

            media_destination.mkdir(
                parents=True,
                exist_ok=True,
            )

            for item in media_backup.iterdir():

                destination = (
                    media_destination
                    / item.name
                )

                if item.is_dir():

                    shutil.copytree(
                        item,
                        destination,
                        dirs_exist_ok=True,
                    )

                else:

                    shutil.copy2(
                        item,
                        destination,
                    )

        return safety_backup

    finally:

        shutil.rmtree(
            temp_dir,
            ignore_errors=True,
        )



def save_backup():

    BACKUP_STORAGE.mkdir(
        parents=True,
        exist_ok=True
    )


    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )


    backup_path = (
        BACKUP_STORAGE
        / f"{BACKUP_PREFIX}{timestamp}.zip"
    )


    return create_backup(
        destination=backup_path
    )