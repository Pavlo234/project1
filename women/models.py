from django.db import models
from django.urls import reverse

class PablishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_publisher=Women.Stutus.PABLISHED) 

class Women(models.Model):
    class Stutus(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PABLISHED = 1, 'Опубликовано'
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_publisher = models.BooleanField(choices=Stutus.choices, default=Stutus.DRAFT)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,related_name='posts')

    objects = models.Manager()
    publisher = PablishedManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug' : self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True )
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug' : self.slug})