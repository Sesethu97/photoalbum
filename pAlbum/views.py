import re
from django.shortcuts import render
from django.views.generic import (
    ListView)
from .models import Images, Story, Categories


# Create your views here.

class Home(ListView):
    model = Images
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        category_menu = Categories.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context
        
def Info(request):
    return render(request, 'info.html', {})


def PhotoAlbum(request):
    return render(request, 'album.html', {})
