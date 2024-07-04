from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world! from Django")

def welcome(request):
    return HttpResponse("Welcome!")

def wish(request):
    return HttpResponse("Good Morning!")

def test(request):
    return HttpResponse("Added git ignore file!")

def message(request):
    return HttpResponse("Git hub action change!")

