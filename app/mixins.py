""" Generic view mixins """


# Create your mixins here.
class OwnerMixin:
    """Adds the owner of the object"""

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserFilterMixin:
    """Filters the queryset by user"""

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
