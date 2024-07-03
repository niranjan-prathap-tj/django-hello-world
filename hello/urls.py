from django.urls import path
from .views import hello_world, welcome, wish, test, message

urlpatterns = [
    path('hello/', hello_world),
    path('',welcome),
    path('wish/',wish),
    path('test/',test),
    path('message/',message)
]

