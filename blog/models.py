from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# ======================================================================================================================
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
# ======================================================================================================================
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category =models.ManyToManyField(Category)
    tags = TaggableManager()
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})

    def __str__(self):
        return self.title
# ======================================================================================================================