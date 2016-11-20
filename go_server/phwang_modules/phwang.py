import go_server.phwang_modules.fabric_modules.fabric
import go_server.phwang_modules.fabric_modules.ajax

def malloc():
    return RootClass()

def malloc_farbric(root_object_val):
    return go_server.phwang_modules.fabric_modules.fabric.malloc(root_object_val)

def malloc_ajax(root_object_val):
    return go_server.phwang_modules.fabric_modules.ajax.malloc(root_object_val)

class RootClass(object):
    def __init__(self):
        self.theFarbricObject = malloc_farbric(self)
        self.theAjaxObject = malloc_ajax(self)
        self.debug(True, "init__", "")

    def objectName(self):
        return "RootClass"

    def farbricObject(self):
        return self.theFarbricObject

    def ajaxObject(self):
        return self.theAjaxObject

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
        go_server.phwang_modules.phwang.utilLogit(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def ABEND(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.phwang.utilAbend(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)



import logging

logger = logging.getLogger(__name__)

def utilLogit(str12, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
    if  str3 == "":
        logger.error(str12)
        return
    if  str4 == "":
        logger.error(str12, str3)
        return
    if  str5 == "":
        logger.error(str12, str3, str4)
        return
    if  str6 == "":
        logger.error(str12, str3, str4, str5)
        return
    if  str7 == "":
        logger.error(str12, str3, str4, str5, str6)
        return
    if  str8 == "":
        logger.error(str12, str3, str4, str5, str6, str7)
        return
    if  str9 == "":
        logger.error(str12, str3, str4, str5, str6, str7, str8)
        return
    if  str10 == "":
        logger.error(str12, str3, str4, str5, str6, str7, str8, str9)
        return
    if  str11 == "":
        logger.error(str12, str3, str4, str5, str6, str7, str8, str9, str10)
        return
    logger.error(str12, str3, str4, str5, str6, str7, str8, str9, str10, str11)


def utilAbend(str12, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
    utilLogit("Abend " + str12, str3, str4, str5, str6, str7, str8, str9, str10, str11)
