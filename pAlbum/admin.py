from django.contrib import admin

from pAlbum.models import Categories, Images, Story

# Register your models here.

admin.site.register(Categories)
admin.site.register(Images)
admin.site.register(Story)