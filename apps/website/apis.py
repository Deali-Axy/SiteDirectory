from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.network import get_ip
from .models import WebSite, ClickLog


@api_view()
def visit(request, pk=None):
    website: WebSite = get_object_or_404(WebSite, pk=pk)

    ClickLog.objects.create(
        website=website,
        ip_address=get_ip(request)
    )

    return Response({
        'message': f'ok, visit {website.name}'
    })
