from django.urls import path

from .views import (
   Home,
   PhotoAlbum,
    
)


app_name = "photoalbum"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("index/", PhotoAlbum, name="albums"),


   
]
