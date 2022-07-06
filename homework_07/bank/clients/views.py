from django.shortcuts import render
from django.http import HttpRequest

from .models import Client


def index(request: HttpRequest):
    """
    TODO
    :param request:
    :return:
    """
    clients = Client.objects.order_by("-id").all()
    context = {
        "clients": clients,
    }
    return render(request, "clients/index.html", context=context)
