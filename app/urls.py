""" Main App URLConf """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.books.views import BookViewSet


# Create your URlConf here.
router = DefaultRouter()
router.register("books", BookViewSet, "book")


urlpatterns = [
    path("", include(router.urls)),
]
