"""TSAWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from TSAWeb_App.views import contact_page, homepage, resources_page, news_page, about_us_page, blog_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('home', homepage, name='home'),
    path('resources', resources_page, name='mission'),
    path('news', news_page, name='projects'),
    path('contact', contact_page, name='contact'),
    path('about_us', about_us_page, name='about us'),
    path("blog", blog_page, name="Blog Posts"),

]
