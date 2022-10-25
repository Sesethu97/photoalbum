from django.contrib import admin

from pAlbum.models import Categories, Image, Story

# Register your models here.

admin.site.register(Categories)
admin.site.register(Image)
admin.site.register(Story)