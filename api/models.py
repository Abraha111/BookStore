from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import CASCADE
import pdfplumber


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Author(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    pdf_file = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    image = models.ImageField(upload_to='images/')
    page_count = models.IntegerField(default=0)
    author = models.ForeignKey('api.Author', CASCADE)
    genre = models.ForeignKey('api.Genre', CASCADE)

    def set_page_book(self):
        with pdfplumber.open(self.pdf_file.path) as pdf:
            self.page_count = len(pdf.pages)

    def save(self, *args, **kwargs):
        self.set_page_book()  # Invoke the page count calculation
        return super().save(*args, **kwargs)


