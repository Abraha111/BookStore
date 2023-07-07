from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from PyPDF2 import PdfReader

from api.models import Book
from api.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = (FormParser, MultiPartParser)

    # def create(self, request, *args, **kwargs):
    #     file = request.FILES.get('file', None)
    #     image = request.FILES.get('image', None)
    #     if file and image:
    #         # Check if the filename is present
    #         if not file.name:
    #             return Response(
    #                 {'error': 'Missing filename. Request should include a filename parameter for the file.'},
    #                 status=status.HTTP_400_BAD_REQUEST)
    #
    #         if not image.name:
    #             return Response(
    #                 {'error': 'Missing filename. Request should include a filename parameter for the image.'},
    #                 status=status.HTTP_400_BAD_REQUEST)
    #
    #         pdf = PdfReader(file)
    #         page_count = len(pdf.pages)
    #
    #         book = Book(title=request.data.get('title'), year=request.data.get('year'), file=file, image=image,
    #                     page_count=page_count, author_id=request.data.get('author'), genre_id=request.data.get('genre'))
    #         book.save()
    #
    #         serializer = self.get_serializer(book)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({'error': 'Both file and image must be uploaded'}, status=status.HTTP_400_BAD_REQUEST)

