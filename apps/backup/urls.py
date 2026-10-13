from django.urls import path

from . import views


app_name = "backup"


urlpatterns = [
    path(
        "",
        views.backup_center,
        name="backup_center",
    ),

    path(
        "download/",
        views.download_backup,
        name="download_backup",
    ),

    path(
        "create/",
        views.create_server_backup,
        name="create_backup",
    ),
    
    path(
        "restore/",
        views.upload_backup,
        name="upload_backup",
    ),



]