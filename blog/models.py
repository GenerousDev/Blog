from django.db import models

from django.db.models.base import Model, ModelState
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=15)
    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description =models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,max_length=150)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(BlogPost,self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return self.slug