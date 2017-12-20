from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    friends = models.ManyToManyField("self")

class Weibo(models.Model):
    user = models.ForeignKey(User, related_name = "weibo", blank = True, null = False)
    content = models.TextField(max_length=1000)
    time = models.DateTimeField()

class Comment(models.Model):
    weibo = models.ForeignKey(Weibo, related_name="comments", blank=True, null=False)
    user = models.ForeignKey(Weibo, related_name="comments", blank=True, null=False)
    time = models.DateTimeField()
