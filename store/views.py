from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h1>hello from my djang + 1+ 1<h1>")


def about(request):
    return HttpResponse("<h2> about <h2>")