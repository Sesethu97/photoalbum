from django.db import models
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    slug = models.SlugField(unique=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("photoalbum:home")

class Image(models.Model):
    caption = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.caption



class Story(models.Model):
    title = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, null=True, blank=True)
    body=models.TextField()

    def __str__(self):
        return self.title
