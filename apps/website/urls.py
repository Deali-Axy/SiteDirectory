from django.urls import path
from . import views
from . import apis

urlpatterns = [
    path('', views.public, name='public'),
    path('private/', views.private, name='private'),
    path('goto/<int:pk>/', views.goto, name='goto'),
    path('search', views.search, name='search'),

    path('api/site/<int:pk>/visit/', apis.visit, name='api_visit'),
]
