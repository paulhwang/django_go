import go_server.project_modules.port_modules.ajax

def malloc(root_val):
    return PortClass(root_val)

def malloc_ajax(port_val):
    return go_server.project_modules.port_modules.ajax.malloc(port_val)

class PortClass(object):
    def __init__(self, root_val):
        self.theRootObject = root_val
        self.theAjaxObject = malloc_ajax(self)

    def className(self):
        return "PortClass"

    def rootObject(self):
        return self.theRootObject

    def ajaxObject(self):
        return self.theAjaxObject

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
