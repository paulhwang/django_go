from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def go_entry(request):
    return HttpResponse("Hello there!")