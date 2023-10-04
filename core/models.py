from django.db import models


# Create your models here.

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    auther = models.CharField(max_length=200, null=False, blank=False)
    publisher = models.CharField(max_length=200, null=False, blank=False)
    number_of_pages = models.IntegerField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/images/", null=True)
    slug = models.SlugField(max_length=200, null=True)
    uploading_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}{self.id}"
