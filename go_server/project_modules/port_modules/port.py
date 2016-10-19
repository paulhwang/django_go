import go_server.project_modules.port_modules.ajax

def malloc(phwang_val):
    return PortClass(phwang_val)

def malloc_ajax(port_val):
    return go_server.project_modules.port_modules.ajax.malloc(port_val)

class PortClass(object):
    def __init__(self, phwang_val):
        self.thePhwangObject = phwang_val
        self.theAjaxObject = malloc_ajax(self)

    def className(self):
        return "PortClass"

    def phwangObject(self):
        return self.thePhwangObject

    def ajaxObject(self):
        return self.theAjaxObject

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.phwangObject().logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.phwangObject().abend(str1 , str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

