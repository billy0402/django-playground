from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import redirect, render

from src.app.authentication.forms import CustomUserForm


def register(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('root')

    form = CustomUserForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, '{} 您好，歡迎使用~'.format(user.username))
        return redirect('root')

    return render(request, 'auth/register.html', {'form': form})
