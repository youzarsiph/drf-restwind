""" Views for app.books """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from app.books.models import Book
from app.books.serializers import BookSerializer
from app.mixins import OwnerMixin
from app.permissions import IsOwner


# Create your views here.
class BookViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Books"""

    queryset = Book.objects.prefetch_related("user")
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["user", "title"]
    search_fields = ["title", "user", "description"]
    ordering_fields = ["title", "created_at", "updated_at"]

    def get_permissions(self):
        """Allow read access to all users"""

        if self.action in ["create", "update", "partial_update", "delete"]:
            self.permission_classes = [IsAuthenticated, IsOwner]

        return super().get_permissions()
