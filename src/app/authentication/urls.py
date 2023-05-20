from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy

from .views import register

login_kwargs = {
    'template_name': 'auth/login.html',
    'redirect_authenticated_user': True,
}

password_reset_kwargs = {
    'template_name': 'auth/password_reset.html',
    'email_template_name': 'auth/password_reset/email.html',
    'subject_template_name': 'auth/password_reset/subject.txt',
    'success_url': reverse_lazy('auth:login'),
}

password_set_kwargs = {
    'template_name': 'auth/password_set.html',
    'post_reset_login': True,
    'success_url': reverse_lazy('auth:login'),
}

app_name = 'auth'
urlpatterns = [
    path('login/', LoginView.as_view(**login_kwargs), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path(
        'password-reset/',
        PasswordResetView.as_view(**password_reset_kwargs),
        name='password_reset',
    ),
    path(
        'password-set/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(**password_set_kwargs),
        name='password_set',
    ),
]
