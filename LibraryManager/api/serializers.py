from rest_framework import serializers
from api.models import Book
from api.models import Book


class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"