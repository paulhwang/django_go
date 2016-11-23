from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import go_server.phwang_modules.util_modules.queue
import go_server.phwang_modules.fabric_modules.root
import go_server.phwang_modules.go_modules.go_root
from django.views.decorators.csrf import csrf_exempt

go_root = go_server.phwang_modules.go_modules.go_root.malloc()
root = go_server.phwang_modules.fabric_modules.root.malloc()

def go_html(request):
    return render(request, "go_django.html")

@csrf_exempt
def go_ajax(request):
    return root.ajaxObject().processInput(request)

def hello_entry(request):
    return HttpResponse("Hello there!")
