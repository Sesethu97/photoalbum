import re
from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, 'home.html', {})


def PhotoAlbum(request):
    return render(request, 'album.html', {})
