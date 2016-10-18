from django.http import JsonResponse
import json

def malloc(port_val):
    return AjaxClass(port_val)

class AjaxClass(object):
    def __init__(self, port_val):
        self.thePortObject = port_val

    def className(self):
        return "AjaxClass"

    def portObject(self):
        return self.thePortObject

    def rootObject(self):
        return self.portObject().rootObject()

    def fibreObject(self):
        return self.rootObject().farbricObject()

    def dispatchObject(self):
        return self.fibreObject().dispatchObject()

    def processInput(self, request_val):
        if not request_val.is_ajax():
            return

        if request_val.method == "POST":
            return self.processPost(request_val)

        if request_val.method == "GET":
            return self.processGet(request_val)

        self.abend("processInput", "not found")
        return JsonResponse({'status':'0'})

    def errorResponse(self):
        return JsonResponse({'status':'0'})

    def processPost(self, request_val):
        self.abend("processPost", "")
        return JsonResponse({'status':'0'})

    def processGet(self, request_val):
        if not request_val:
            return self.errorResponse()

        json_request = request_val.META.get("HTTP_GOREQUEST")
        if not json_request:
            self.abend("processGet", "null json_request")
            return self.errorResponse()
        self.debug(False, "processGet", "HTTP_GOREQUEST=%s", json_request)

        go_request = json.loads(json_request)
        if not go_request:
            self.abend("processGet", "null go_request")
            return
        self.debug(False, "processGet", "go_request=%s", go_request)
        self.debug(False, "processGet", "command=%s", go_request["command"])

        if go_request["command"] != "keep_alive" and go_request["command"] != "get_name_list" and go_request["command"] != "get_link_data" and go_request["command"] != "get_session_data":
            self.debug(True, "processGet", "command=%s", go_request["command"])

        data = self.dispatchObject().dispatchRequest(go_request)
        json_str = json.dumps({
                        "command": go_request["command"],
                        "ajax_id": go_request["ajax_id"],
                        "data": data,
                        "res_data": data,
                    })
        #res.type('application/json')
        #res.send(json_str)
        #return JsonResponse({'status':'0'})
        return JsonResponse({
                        "command": go_request["command"],
                        "ajax_id": go_request["ajax_id"],
                        "data": data,
                        "res_data": data,
                    })

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.portObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.portObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

