import go_server.phwang_modules.fabric_modules.link_mgr
import go_server.phwang_modules.fabric_modules.cluster_mgr
import go_server.phwang_modules.fabric_modules.switch

def malloc(root_object_val):
    return FibreClass(root_object_val)

def malloc_link_mgr(root_object_val):
    return go_server.phwang_modules.fabric_modules.link_mgr.malloc(root_object_val)

def malloc_cluster_mgr(root_object_val):
    return go_server.phwang_modules.fabric_modules.cluster_mgr.malloc(root_object_val)

def malloc_switch(root_object_val):
    return go_server.phwang_modules.fabric_modules.switch.malloc(root_object_val)

class FibreClass(object):
    def __init__(self, root_object_val):
        self.theRootObject = root_object_val
        self.theLinkMgrObject = malloc_link_mgr(self.rootObject())
        self.theClusterMgrObject = malloc_cluster_mgr(self.rootObject())
        self.theSwitchObject = malloc_switch(self.rootObject())
        self.debug(True, "init__", "")

    def objectName(self):
        return "FibreClass"

    def rootObject(self):
        return self.theRootObject

    def linkMgrObject(self):
        return self.theLinkMgrObject

    def sessionMgrObject(self):
        return self.theSessionMgrObject

    def clusterMgrObject(self):
        return self.theClusterMgrObject

    def switchObject(self):
        return self.theSwitchObject

    def utilObject(self):
        return self.rootObject().utilObject()

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

