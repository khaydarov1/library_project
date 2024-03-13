from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


# Create your views here.


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
              'status': 'Success',
              'book': serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {'status': 'Not Id ',
                 'message': 'Book is not found'},status=status.HTTP_404_NOT_FOUND
            )


class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': ' success',
                'books': data,
            }
            return Response(data)
        else:
            return Response(
                {'status': False,
                 'message': "Serializer is not valid"},status=status.HTTP_400_BAD_REQUEST
            )

class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            'books': serializer_data
        }
        return Response(data)
