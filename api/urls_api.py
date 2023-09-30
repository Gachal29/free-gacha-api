from django.urls import path

from .views_api import GachalAPI

urlpatterns = [
    path("gachal/", GachalAPI.as_view(), name="gachal"),
]
