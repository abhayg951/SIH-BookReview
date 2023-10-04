from rest_framework.views import APIView
from .models import Book
from .serializers import BookListSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.

class BookList(APIView):
    @staticmethod
    def get(request):
        book = Book.objects.all()
        serializer = BookListSerializer(book, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetails(APIView):
    @staticmethod
    def get_object(slug):
        try:
            return Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        book = self.get_object(slug)
        serializer = BookListSerializer(book)
        return Response(serializer.data)

    def post(self, request, slug):
        book = self.get_object(slug)
        serializer = BookListSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        book = self.get_object(slug)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
