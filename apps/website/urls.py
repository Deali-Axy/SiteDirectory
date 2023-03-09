from django.urls import path
from . import views

urlpatterns = [
    path('', views.public, name='public'),
    path('private/', views.private, name='private'),
    path('goto/<int:pk>/', views.goto, name='goto'),
]
