from django.urls import path
from .views import hello_world, welcome, wish

urlpatterns = [
    path('hello/', hello_world),
    path('',welcome),
    path('wish/',wish)
]

