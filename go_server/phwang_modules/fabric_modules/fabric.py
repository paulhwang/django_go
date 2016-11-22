import go_server.phwang_modules.fabric_modules.link_mgr
import go_server.phwang_modules.fabric_modules.cluster_mgr
import go_server.phwang_modules.fabric_modules.switch

def malloc(root_object_val):
    return FibreClass(root_object_val)

class FibreClass(object):
    def __init__(self, root_object_val):
        self.theRootObject = root_object_val
        self.debug(True, "init__", "")

    def objectName(self):
        return "FibreClass"

    def rootObject(self):
        return self.theRootObject

    def utilObject(self):
        return self.rootObject().utilObject()

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

