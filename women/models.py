from django.db import models
from django.urls import reverse

class PablishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_publisher=True) 

class Women(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_publisher = models.BooleanField(default=True)

    objects = models.Manager()
    publisher = PablishedManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug' : self.slug})
