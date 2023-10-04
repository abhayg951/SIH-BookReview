from rest_framework import serializers
from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
