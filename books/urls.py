from django.contrib import admin
from django.urls import path, include
from books.views import *


app_name='book'
urlpatterns = [
      path('book/create/', BookCreateView.as_view())
]
