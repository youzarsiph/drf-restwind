""" App configuration for app.books """

from django.apps import AppConfig


# Create your AppConfig here.
class BooksConfig(AppConfig):
    """AppConfig for app.books"""

    name = "app.books"
    default_auto_field = "django.db.models.BigAutoField"
