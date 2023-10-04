from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Book
from django.utils.text import slugify
import random
import string


@receiver(pre_save, sender=Book)
def add_slug(sender, instance, *args, **kwargs):
    n = 20

    if instance and not instance.slug:
        string1 = slugify(instance.name)
        string2 = slugify(''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                                                 string.ascii_letters +
                                                 string.digits, k=n)))
        instance.slug = string1 + string2
