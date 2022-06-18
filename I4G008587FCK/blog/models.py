from cgitb import text
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    create_date=models.DateTimeField()
    publish_date=models.DateTimeField()

