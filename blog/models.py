from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# import string

class CustomeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='draft')

class BlogTable(models.Model):
    STATUS_CHOICE = (('draft','Draft'),('publised','Published'))
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=264)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.DO_NOTHING)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    objects = CustomeManager()

    class Meta:
        ordering =('-publish',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_details", args={self.slug})
    

