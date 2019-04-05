from django.shortcuts import render

# Create your views here.
# ce/views.py
# Define view
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World 123!")