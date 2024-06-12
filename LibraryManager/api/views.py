from django.shortcuts import render
from rest_framework import viewsets
from api.models import Book
from api.serializers import BookSerializers

# Create your views here.


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers