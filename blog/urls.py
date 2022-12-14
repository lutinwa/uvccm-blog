from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>", views.show, name="show"),
    path("contact", views.contact, name="contact"),
    path("uongozi", views.uongozi, name="uongozi"),
    path("malengo", views.malengo, name="malengo"),
]
