from django.contrib import admin, messages  
from .models import Women, Category
from django.utils.safestring import mark_safe

class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщины'
    parameter_name = 'status'
    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)

@admin.register(Women)
class Womenadmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content','photo', 'post_photo', 'cat','husband', 'tags']
    list_display = ('title','post_photo', 'time_create', 'is_publisher','cat')
    list_display_links = ('title',)
    readonly_fields = ['post_photo']
    ordering = ('time_create', 'title')
    list_editable = ('is_publisher', )
    search_fields = ['title']
    list_filter = [MarriedFilter, 'cat__name', 'is_publisher',]
    filter_horizontal = ['tags']

    @admin.display(description='Краткое описание', ordering='content')
    def post_photo(self, women:Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")
        return 'Без фото'
    
@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

