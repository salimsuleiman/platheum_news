from statistics import mode
from unicodedata import category
from django.db import models
from django_quill.fields import QuillField

from users.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.title



class Post(models.Model):
    
    title = models.CharField(max_length=200)
    body =  QuillField()
    created_at = models.DateTimeField(auto_now=True, verbose_name='Date Created')
    is_published = models.BooleanField(default=True)   
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, default=None, null=True, on_delete=models.SET_NULL)
    writer = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    
    
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True, verbose_name='Date Created')
    author = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
