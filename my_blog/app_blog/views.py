from django.shortcuts import render

from django.shortcuts import render

from app_blog.models import PostCategory, Post


def index(request):
    context = {
        'title': 'Main',
        'posts': Post.objects.all(),
        'categories': PostCategory.objects.all()
    }
    return render(request, 'app_blog/index.html', context)


def about(request):
    return render(request, 'app_blog/about.html')


def contact(request):
    return render(request, 'app_blog/contact.html')
