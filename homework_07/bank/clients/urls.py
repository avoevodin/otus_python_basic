from django.urls import path

app_name = "clients"

urlpatterns = [
    path("", index, name="list"),
]
