from django.db import models
from django.urls import reverse

class PablishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_publisher=Women.Stutus.PABLISHED) 

class Women(models.Model):
    class Stutus(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PABLISHED = 1, 'Опубликовано'
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=120, unique=True, db_index=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name = 'Фото')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_publisher = models.BooleanField(choices=tuple(map(lambda x:(bool(x[0]),x[1]), Stutus.choices)), default=Stutus.PABLISHED)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,related_name='posts')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name='wumen')
    objects = models.Manager() 
    publisher = PablishedManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug' : self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True )
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug' : self.slug})
    
class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag
    
    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug' : self.slug})
    
class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)


    def __str__(self):
        return self.name

class UploudFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')



# from django.db import models
# from django.urls import reverse

# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_publisher=Women.Status.PUBLISHED)  # исправлено

# class Women(models.Model):
#     class Status(models.IntegerChoices):
#         DRAFT = 0, 'Черновик'
#         PUBLISHED = 1, 'Опубликовано'
    
#     title = models.CharField(max_length=200, verbose_name='Заголовок')
#     slug = models.SlugField(max_length=120, unique=True, db_index=True)
#     content = models.TextField(blank=True, verbose_name='Текст статьи')
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_publisher = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)  # исправлено
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
#     tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
#     husband = models.OneToOneField('Husband', on_delete=models.SET_NULL,
#                                    null=True, blank=True, related_name='women')  # исправлено

#     objects = models.Manager()
#     publisher = PublishedManager()

#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         return reverse('post', kwargs={'post_slug': self.slug})

# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)

#     class Meta:
#         verbose_name = 'Категории'
#         verbose_name_plural = 'Категории'

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('category', kwargs={'cat_slug': self.slug})

# class TagPost(models.Model):
#     tag = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)

#     def __str__(self):
#         return self.tag
    
#     def get_absolute_url(self):
#         return reverse('tag', kwargs={'tag_slug': self.slug})

# class Husband(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField(null=True)
#     m_count = models.IntegerField(blank=True, default=0)

#     def __str__(self):
#         return self.name + ' , '  # исправлено
