""" Custom access permissions """

from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsOwner(BasePermission):
    """Custom permission to only allow owners of an object to edit or delete it."""

    def has_object_permission(self, request, view, obj) -> bool:
        """Check if the user is the owner of the object"""

        return obj.user == request.user
