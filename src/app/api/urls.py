from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.trailing_slash = ''
router.register('books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
