from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, WebSite, ClickLog


def get_ip(request):
    """
    获取IP地址
    参考：https://pythonguides.com/get-user-ip-address-in-django/

    :param request:
    :return:
    """
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def public(request):
    theme = request.GET.get('theme', 'standard')
    template = 'public.html'
    if theme == 'simple':
        template = 'public_simple.html'

    ctx = {
        'categories': Category.objects.all(),
    }

    return render(request, template, ctx)


def private(request):
    return render(request, 'private.html')


def goto(request, pk=None):
    website: WebSite = get_object_or_404(WebSite, pk=pk)

    ClickLog.objects.create(
        website=website,
        ip_address=get_ip(request)
    )

    return redirect(website.url)
