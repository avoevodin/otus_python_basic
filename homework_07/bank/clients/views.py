from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from .models import Client


def index(request: HttpRequest):
    """
    TODO
    :param request:
    :return:
    """
    clients = Client.objects.select_related("details").order_by("-id").all()
    context = {
        "clients": clients,
    }
    return render(request, "clients/index.html", context=context)


def details(request: HttpRequest, pk: int):
    """
    TODO
    :param request:
    :param pk:
    :return:
    """

    client = get_object_or_404(
        Client.objects.select_related(
            "job",
            "details",
        ).prefetch_related("services"),
        pk=pk,
    )
    context = {"client": client}
    return render(request, "clients/details.html", context=context)
