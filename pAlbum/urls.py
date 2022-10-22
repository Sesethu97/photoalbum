from django.urls import path

from .views import (
   Home,
   Info,
   PhotoAlbum,
    
)


app_name = "photoalbum"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("info/", Info, name="info"),
    path("index/", PhotoAlbum, name="albums"),




   
]
