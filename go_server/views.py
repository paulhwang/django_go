from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_entry(request):
    return HttpResponse("Hello there!")

def go_entry(request):
    return render(request, "js_go/phwang.html")