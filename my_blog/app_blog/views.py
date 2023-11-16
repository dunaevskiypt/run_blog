from django.shortcuts import render

from django.shortcuts import render


def index(request):
    return render(request, 'app_blog/index.html')


def about(request):
    return render(request, 'app_blog/about.html')


def contact(request):
    return render(request, 'app_blog/contact.html')
