from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status, viewsets


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

class BookUpdateApiView(APIView):
    def put(self, request,pk):
        book=get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(
            instance=book,data=data,partial=True )
        if serializer.is_valid(raise_exception=True):
            book_save=serializer.save()
        return Response(
            {'status': True,
             'message': f'Book {book_save} updated successfully'
             }
        )



class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    'status': True,
                    'message': 'Successfully deleted'
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response({
                    'status': False,
                    'message': 'Book is not found'
            }, status=status.HTTP_400_BAD_REQUEST)


class BookListApiView(viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        # Your custom action logic here
        return Response("Custom action response")



# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class =BookSerializer
