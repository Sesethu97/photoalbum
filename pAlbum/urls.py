from django.urls import path

from .views import (
   HomePage,
   PhotoAlbum,
    
)


app_name = "photoalbum"

urlpatterns = [
    path("", HomePage, name="home"),
    path("index/", PhotoAlbum, name="albums"),


   
]
