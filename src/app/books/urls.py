from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<str:pk>/', views.show, name='show'),
    path('<str:pk>/edit/', views.edit, name='edit'),
    path('<str:pk>/delete/', views.delete, name='delete'),
]
