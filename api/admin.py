from django.contrib import admin
from .models import Genre, Author, Book

admin.site.register(Genre)
admin.site.register(Author)


@admin.register(Book)
class Book(admin.ModelAdmin):

    class Meta:
        model = Book
        fields = '__all__'









