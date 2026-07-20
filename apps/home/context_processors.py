from .models import NavbarLogo, NavbarMenu


def navbar(request):
    return {
        "navbar": NavbarLogo.objects.first(),

        "menu": NavbarMenu.objects.filter(
            activo=True,
            padre__isnull=True
        ).order_by("orden"),
    }