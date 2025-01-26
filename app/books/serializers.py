""" Serializers for app.books """

from rest_framework.serializers import ModelSerializer

from app.books.models import Book


# Create your serializers here.
class BookSerializer(ModelSerializer):
    """Serializer for Book model"""

    class Meta:
        """Meta data"""

        model = Book
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
