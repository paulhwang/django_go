from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import go_server.phwang_modules.fabric_modules.root

def go_html(request):
    return render(request, "go_django.html")

@csrf_exempt
def go_ajax(request):
    return go_server.phwang_modules.fabric_modules.root.process_ajax_input(request)

def hello_entry(request):
    return HttpResponse("Hello there!")
