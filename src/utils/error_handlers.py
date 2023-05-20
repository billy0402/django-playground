from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render


def permission_denied(
    request: HttpRequest,
    exception: Exception,
    template_name='403.html',
):
    messages.warning(request, '權限不足')
    return redirect('root')


def page_not_found(
    request: HttpRequest,
    exception: Exception,
    template_name='404.html',
):
    return render(request, 'errors/404.html', status=404)
