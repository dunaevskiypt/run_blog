from django.db import models

from django.db import models


class PostCategory (models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.name


class Post (models.Model):
    image = models.ImageField(upload_to='product_images')
    image_2 = models.ImageField(upload_to='product_images')
    image_extra = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(to=PostCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=500)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'Post:{self.title} | Categoty {self.category.name} '
