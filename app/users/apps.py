""" App configuration for app.users """

from django.apps import AppConfig


# Create your AppConfig here.
class UsersConfig(AppConfig):
    """AppConfig for app.users"""

    name = "app.users"
    default_auto_field = "django.db.models.BigAutoField"
