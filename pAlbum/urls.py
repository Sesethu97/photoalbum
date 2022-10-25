from django.urls import path

from .views import (
   Home,
   Info,
   album
)


app_name = "album"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("info/", Info, name="info"),
    path("index/", album, name="albums"),




   
]
