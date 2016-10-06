from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

html_count = 0
def go_html(request):
    global html_count
    html_count += 1
    logger.error("go_html %s", html_count)
    return render(request, "js_go/phwang.html")

ajax_count = 0
#@csrf_exempt
def go_ajax(request):
    global ajax_count
    ajax_count += 1
    logger.error("ajax_count %s", ajax_count)
    return render(request, "js_go/phwang.html")

def hello_entry(request):
    return HttpResponse("Hello there!")
