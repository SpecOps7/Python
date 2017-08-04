from django.shortcuts import render
from django.htp import HttpResponse as webResponse

def index(request):
    return webResponse("<h2>HEY!</h2>")

# Create your views here.
