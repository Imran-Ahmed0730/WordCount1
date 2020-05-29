
from django.urls import path
from . import view

urlpatterns = [
    path("", view.home, name = "homepage"),
    path("Count/", view.count, name = "Counting"),
    path("about/", view.about, name = "about")
]
