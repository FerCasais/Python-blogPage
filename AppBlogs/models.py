from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from ckeditor.fields import RichTextField


# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=256)
    subTitle = models.CharField(max_length=256)
    body = RichTextField()
    author = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(max_length=300, upload_to="blogImages", null=True, blank=True)
   
    
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title}, {self.subTitle}"

