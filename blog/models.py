from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
