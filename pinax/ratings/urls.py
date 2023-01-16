from django.urls import path

from pinax.ratings import views

app_name = "pinax_ratings"


urlpatterns = [
    path("(<int:content_type_id>)/<int:object_id>)/rate/", views.RateView.as_view(), name="rate"),
]
