from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    #article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True, blank=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.ManyToManyField('Comment', related_name='article_comments')

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    description = models.TextField()
