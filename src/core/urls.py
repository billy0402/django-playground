"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

admin.site.site_title = '書店 網站管理'
admin.site.site_header = '書店 管理'

urlpatterns = [
    path('', lambda request: redirect('books:index'), name='root'),
    path('books/', include('src.app.books.urls')),
    path('auth/', include('src.app.authentication.urls')),

    path('api/', include('src.app.api.urls')),
    path(
        'api/auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),
    path('api/auth/token', obtain_auth_token, name='api_auth'),

    path('admin/', admin.site.urls),
]

handler403 = 'src.utils.error_handlers.permission_denied'
handler404 = 'src.utils.error_handlers.page_not_found'
