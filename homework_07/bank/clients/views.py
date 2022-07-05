from django.shortcuts import render
from django.http import HttpRequest

from .models import Client


def index(request: HttpRequest):
    clients = Client.objects.order_by("-id").all()
    print(clients)
