""" Data Models """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Book(models.Model):
    """A simple model"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="books",
        help_text="Book author",
    )
    title = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Book title",
    )
    description = models.TextField(
        help_text="Book title",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Book creation date",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Book update date",
    )

    def __str__(self):
        return self.title
