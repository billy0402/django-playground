from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.trailing_slash = ''
router.register('authors', views.AuthorViewSet)
router.register('publishers', views.PublisherViewSet)
router.register('classifications', views.ClassificationViewSet)
router.register('tags', views.TagViewSet)
router.register('books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
