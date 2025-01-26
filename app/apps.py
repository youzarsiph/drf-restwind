""" App configuration """

from django.apps import AppConfig


# Create your AppConfig here.
class AppConfig(AppConfig):
    """Main AppConfig"""

    name = "app"
    default_auto_field = "django.db.models.BigAutoField"
