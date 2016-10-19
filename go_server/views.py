from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import go_server.phwang_modules.util_modules.queue
import go_server.phwang_modules.phwang
from django.views.decorators.csrf import csrf_exempt

phwang = go_server.phwang_modules.phwang.malloc()

def go_html(request):
    return render(request, "go_django.html")

@csrf_exempt
def go_ajax(request):
    return phwang.portObject().ajaxObject().processInput(request)

def hello_entry(request):
    return HttpResponse("Hello there!")
