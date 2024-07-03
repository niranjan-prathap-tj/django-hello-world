from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world! from Django")

def welcome(request):
    return HttpResponse("Welcome!")

def wish(request):
    return HttpResponse("Good Morning!")

def test(request):
    return HttpResponse("tagged version v1.1")

def message(request):
    return HttpResponse("Git hub action change!")

