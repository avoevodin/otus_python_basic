from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    TODO
    """

    list_display = (
        "first_name",
        "middle_name",
        "last_name",
        "birthday",
    )

    list_display_links = (
        "first_name",
        "middle_name",
        "last_name",
    )
