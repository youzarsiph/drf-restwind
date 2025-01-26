""" Serializers for app.Users """

from rest_framework.serializers import ModelSerializer

from app.users.models import User


# Create your serializers here.
class UserSerializer(ModelSerializer):
    """Serializer for User model"""

    class Meta:
        """Meta data"""

        model = User
        fields = ["id", "image", "username", "first_name", "last_name"]
