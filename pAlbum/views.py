from contextlib import redirect_stderr
import re
from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
from django.views.generic import (
    ListView)

from .forms import ImageForms
from .models import Image, Categories


# Create your views here.

class Home(ListView):
    model = Image
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        category_menu = Categories.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context
        
def Info(request):
    return render(request, 'info.html', {})

def album(request: HttpRequest):
    posts = Image.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'album.html', context)

def PhotoAlbum(request):
    
    return render(request, 'album.html', {})
