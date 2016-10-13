from django.http import JsonResponse

def malloc(port_val):
    return AjaxClass(port_val)

class AjaxClass(object):
    def __init__(self, port_val):
        self.thePortObject = port_val

    def className(self):
        return "AjaxClass"

    def portObject(self):
        return self.thePortObject

    def processInput(self, request_val):
        return JsonResponse({'status':'0'})
