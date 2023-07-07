# from rest_framework.serializers import ModelSerializer
#
# from api.models import Book, BookImage, Genre, Author
#
#
# class GenreSerializer(ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = '__all__'
#
#
# class AuthorSerializer(ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#
# class BookImageSerializer(ModelSerializer):
#     class Meta:
#         model = BookImage
#         fields = '__all__'
#
#
# class BookSerializer(ModelSerializer):
#     author = AuthorSerializer()
#     genre = GenreSerializer()
#     images = BookImageSerializer(many=True)
#
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#
#

from rest_framework import serializers
from .models import Genre, Author, Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    # genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    # images = BookImageSerializer()

    class Meta:
        model = Book
        fields = "__all__"




















