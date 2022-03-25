from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import BookViewSet

router = SimpleRouter(trailing_slash=False)
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
