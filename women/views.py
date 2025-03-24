from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from women.models import Women
from .models import Women, Category, TagPost


menu = [
    {'title': 'О сайте', 'url_name' :'about'},
    {'title': 'Добавить статью', 'url_name' : 'add_page'},
    {'title': 'Обратная связь', 'url_name' :'contact'},
    {'title': 'Войти', 'url_name' :'login',
}]

data_db = [
    {'id' : 1, 'title' : 'Анджелина Джоли', 'content' : '''Анджелина Джоли — американская актриса''' , 'is_published' : True,},
    {'id' : 2, 'title' : 'biry', 'content' : 'История мороженого' ,'is_published' : True,},
    {'id' : 3, 'title' : 'roma', 'content' : 'майнкрафт' ,'is_published' : True,},
]


def index(request):
    posts = Women.publisher.all()
    data =  {
        'title' : 'Главная  страница',
        'menu' : menu,
        'posts' : posts,
        'cat_selected' : 0,
        }
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title' : 'главная о нас', 'menu': menu})

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Зарегистрироваться')

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug = cat_slug)
    posts = Women.publisher.filter(cat_id = category.pk)
    data =  {
        'title' : f'Отображение статьи {category.name}',
        'menu' : menu,
        'posts' : posts,
        'cat_selected' : category.pk,
        }
    return render(request, 'women/index.html', context=data)









def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data =  {
        'title' : post.title,
        'menu' : menu,
        'post' : post,
        'cat_selected' : 1,
        }
    return render(request, 'women/post.html', data)



def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_publisher=Women.Stutus.PABLISHED)

    data={
        'title': f'Тег: {tag.tag}',
        'menu' : menu,
        'posts': posts,
        'cat_selected' : None,
    }
    return render(request, 'women/index.html', context=data)
