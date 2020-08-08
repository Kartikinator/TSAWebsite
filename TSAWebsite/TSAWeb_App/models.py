from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Officer(models.Model):
    officer_name = models.CharField(max_length=150)
    role = models.CharField(max_length=100)
    description = models.TextField(max_length=450)
    imageurl = models.URLField(default="")

    def __str__(self):
        return self.officer_name
