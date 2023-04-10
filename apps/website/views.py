from django.shortcuts import render, get_object_or_404, redirect
from utils.network import get_ip

from .models import Category, WebSite, ClickLog


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

    return redirect(website.url, permanent=True)


def search(request):
    keyword = request.GET.get('q', '')
    return redirect(f'https://www.bing.com/search?q={keyword}')
