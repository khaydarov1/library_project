from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'content', 'subtitle', 'isbn', 'price',)


    def validate(self, data):
        title = data.get('title',None)
        author = data.get('author',None)



        # alphabetical chars
        if not title.isalpha():
            raise ValidationError({
                'status': False,
                'message': 'Kitobni sarlavhasi harflardan tashkin topishi kerak'
            })



        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False
                    'message': 'Kitob sarlavhasi va mualifi bir xil bolsa yuklay olmaysiz'
                }
            )
        return data

    def validate_price(self, price):
        if price <0 or price >99999999999:
            raise ValidationError({
                'status': False
                'message': 'Narx '
            })