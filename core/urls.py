from django.urls import path
from .views import BookList, SingleBookDetails

urlpatterns = [
    path('book', BookList.as_view()),
    path('book/<slug:slug>', SingleBookDetails.as_view())
]