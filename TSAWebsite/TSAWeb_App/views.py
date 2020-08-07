from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost


# Create your views here.
def homepage(request, *args, **kwargs):
    return render(request, "homepage.html", {})


def resources_page(request, *args, **kwargs):
    return render(request, "resources.html", {})


def news_page(request, *args, **kwargs):
    return render(request, "news.html", {})


def contact_page(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_us_page(request, *args, **kwargs):
    return render(request, "about_us.html", {})


def blog_page(request, *args, **kwargs):
    return render(request, "blog_posts.html", context={"blog_post": BlogPost.objects.all})
