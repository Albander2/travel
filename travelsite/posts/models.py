from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=None)
    growth = models.IntegerField(default=None)
    weight = models.IntegerField(default=None)
    price = models.IntegerField(default=None)
    breast_size = models.IntegerField(default=None)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class PostImage(models.Model):
    post = models.ForeignKey(Post,default=None, on_delete=models.CASCADE, verbose_name='product_image')
    image = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.post.name
