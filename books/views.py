from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from books.serializers import BookDetailSerializer


class BookCreateView(generics.CreateAPIView):
    serializer_class=BookDetailSerializer