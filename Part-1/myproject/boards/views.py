from django.shortcuts import render
# This is for add a HTTP response.
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello, World!')