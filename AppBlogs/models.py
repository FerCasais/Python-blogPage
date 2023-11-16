from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=256)
    subTitle = models.CharField(max_length=256)
    body = models.CharField(max_length=256)
    author = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(null=True)
    image = models.CharField(max_length=32)
    


    def __str__(self):
        return f"{self.title}, {self.subTitle}"
