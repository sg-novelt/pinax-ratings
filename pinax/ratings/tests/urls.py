from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("", include("pinax.ratings.urls", namespace="pinax_ratings")),
]
