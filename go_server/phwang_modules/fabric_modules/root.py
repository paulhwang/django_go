import go_server.phwang_modules.fabric_modules.link_mgr
import go_server.phwang_modules.fabric_modules.cluster_mgr
import go_server.phwang_modules.fabric_modules.switch
import go_server.phwang_modules.fabric_modules.ajax
import go_server.phwang_modules.util_modules.logit
import go_server.phwang_modules.go_modules.go_root

def malloc(go_root_object):
    return RootClass(go_root_object)

def malloc_link_mgr(root_object_val):
    return go_server.phwang_modules.fabric_modules.link_mgr.malloc(root_object_val)

def malloc_cluster_mgr(root_object_val):
    return go_server.phwang_modules.fabric_modules.cluster_mgr.malloc(root_object_val)

def malloc_switch(root_object_val):
    return go_server.phwang_modules.fabric_modules.switch.malloc(root_object_val)

def malloc_ajax(root_object_val):
    return go_server.phwang_modules.fabric_modules.ajax.malloc(root_object_val)

class RootClass(object):
    def __init__(self, go_root_object):
        self.theGoRootObject = go_root_object;
        self.theLinkMgrObject = malloc_link_mgr(self)
        self.theClusterMgrObject = malloc_cluster_mgr(self)
        self.theSwitchObject = malloc_switch(self)
        self.theAjaxObject = malloc_ajax(self)
        self.debug(True, "init__", "")

    def objectName(self):
        return "RootClass"

    def goRootObject(self):
        return self.theGoRootObject

    def linkMgrObject(self):
        return self.theLinkMgrObject

    def clusterMgrObject(self):
        return self.theClusterMgrObject

    def switchObject(self):
        return self.theSwitchObject

    def ajaxObject(self):
        return self.theAjaxObject

    def mallocQueue(self):
        return go_server.phwang_modules.util_modules.queue.malloc(self)

    def mallocRing(self):
        return go_server.phwang_modules.util_modules.ring.malloc(self)

    def mallocBase(self):
        return go_server.phwang_modules.go_modules.go_root.malloc_base()

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def LOG_IT(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.logit.utilLogit(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def ABEND(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.logit.utilAbend(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
