from django.urls import path
from .views import hello_world, welcome, wish, test, message, check_db_connection

urlpatterns = [
    path('hello/', hello_world),
    path('',welcome),
    path('wish/',wish),
    path('test/',test),
    path('message/',message),
    path('dbcon/',check_db_connection)
]

