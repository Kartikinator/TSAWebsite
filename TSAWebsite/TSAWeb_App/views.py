from django.http import HttpResponse
from django.shortcuts import render


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
