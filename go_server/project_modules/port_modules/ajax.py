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
        self.debug(True, "processInput", "method=%s", request_val.method)
        self.debug(True, "processInput", "is_ajax=%i", request_val.is_ajax())
        self.debug(True, "processInput", "GET=%s", request_val.GET)
        self.debug(True, "processInput", "POST=%s", request_val.POST)

        if request_val.method == "POST":
            self.processPost(request_val)

        if request_val.method == "GET":
            return self.processGet(request_val)

        self.abend("processInput", "not found")
        return JsonResponse({'status':'0'})

    def processPost(self, request_val):
        self.abend("processPost", "")
        return JsonResponse({'status':'0'})

    def processGet(self, request_val):
        self.debug(True, "processGet", "command=%s", request_val.GET.get("command"))
        self.debug(True, "processGet", "body=%s", request_val.body)
        #self.debug(True, "processGet", "content=%s", request_val.content_params)
        return JsonResponse({'status':'0'})

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.portObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.portObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

