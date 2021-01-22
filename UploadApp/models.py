from django.db import models

# Create your models here.

class UploadImage(models.Model):
    pic = models.ImageField(upload_to="images")
    name = models.CharField(max_length=100,default="image")