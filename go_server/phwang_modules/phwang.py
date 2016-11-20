import go_server.phwang_modules.util_modules.util
import go_server.phwang_modules.fabric_modules.fabric
import go_server.phwang_modules.port_modules.port

def malloc():
    return RootClass()

def malloc_util(phwang_val):
    return go_server.phwang_modules.util_modules.util.malloc(phwang_val)

def malloc_farbric(phwang_val):
    return go_server.phwang_modules.fabric_modules.fabric.malloc(phwang_val)

def malloc_port(phwang_val):
    return go_server.phwang_modules.port_modules.port.malloc(phwang_val)

class RootClass(object):
    def __init__(self):
        self.theUtilObject = malloc_util(self)
        self.theFarbricObject = malloc_farbric(self)
        self.thePortObject = malloc_port(self)
        self.debug(True, "init__", "")

    def objectName(self):
        return "RootClass"

    def utilObject(self):
        return self.theUtilObject

    def farbricObject(self):
        return self.theFarbricObject

    def portObject(self):
        return self.thePortObject

    def goObject(self):
        return self.theGoObject

    def mallocQueue(self):
        return go_server.phwang_modules.util_modules.queue.malloc(self)

    def mallocRing(self):
        return go_server.phwang_modules.util_modules.ring.malloc(self)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def LOG_IT(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.util.utilLogit(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def ABEND(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.util.utilAbend(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
