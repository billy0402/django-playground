from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import (
    AuthorViewSet,
    BookViewSet,
    ClassificationViewSet,
    PublisherViewSet,
    TagViewSet,
)

router = SimpleRouter(trailing_slash=False)
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('publishers', PublisherViewSet)
router.register('classifications', ClassificationViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
