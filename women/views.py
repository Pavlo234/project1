from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from women.models import Women
from .models import Women, Category, TagPost, UploudFiles
from .forms import AddPostForm, UploadFileForm

menu = [
    {'title': 'О сайте', 'url_name' :'about'},
    {'title': 'Добавить статью', 'url_name' : 'add_page'},
    {'title': 'Обратная связь', 'url_name' :'contact'},
    {'title': 'Войти', 'url_name' :'login',
}]


def index(request):
    posts = Women.publisher.all()
    data =  {
        'title' : 'Главная  страница',
        'menu' : menu,
        'posts' : posts,
        'cat_selected' : 0,
        }
    return render(request, 'women/index.html', context=data)

# def handle_uploaded_file(f):
#     with open(f"uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploudFiles(file=form.cleaned_data['file'])
            fp.save()

    else:
        form = UploadFileForm()
    return render(request, 'women/about.html', {'title' : 'главная о нас', 'menu': menu, 'form' : form})



def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    data = {
        'title' : 'Добавление статьи',
          'menu': menu,
          'form' : form,
    }
    return render(request, 'women/addpage.html',data )

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
