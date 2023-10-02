from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200, null=False)
    auther = models.CharField(max_length=200, null=False)
    publisher = models.CharField(max_length=200, null=False)
    number_of_pages = models.IntegerField()
    image = models.ImageField(upload_to="static/images/")
    slug = models.SlugField(unique=True, null=True)
    uploading_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
