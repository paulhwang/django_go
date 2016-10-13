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
        if request_val.POST:
            processPost(request_val)

        if request_val.GET:
            processGet(request_val)

        self.debug(True, "processInput", "not found")
        return JsonResponse({'status':'0'})

    def processPost(self, request_val):
        self.debug(True, "processPost", "")

    def processGet(self, request_val):
        self.debug(True, "processPost", "")

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.portObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.portObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

