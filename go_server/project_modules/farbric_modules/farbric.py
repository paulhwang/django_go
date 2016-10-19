import go_server.project_modules.farbric_modules.link_mgr
import go_server.project_modules.farbric_modules.session_mgr
import go_server.project_modules.farbric_modules.cluster_mgr
import go_server.project_modules.farbric_modules.switch

def malloc(phwang_val):
    return FibreClass(phwang_val)

def malloc_link_mgr(phwang_val):
    return go_server.project_modules.farbric_modules.link_mgr.malloc(phwang_val)

def malloc_session_mgr(phwang_val):
    return go_server.project_modules.farbric_modules.session_mgr.malloc(phwang_val)

def malloc_cluster_mgr(phwang_val):
    return go_server.project_modules.farbric_modules.cluster_mgr.malloc(phwang_val)

def malloc_switch(phwang_val):
    return go_server.project_modules.farbric_modules.switch.malloc(phwang_val)

class FibreClass(object):
    def __init__(self, phwang_val):
        self.thePhwangObject = phwang_val
        self.theLinkMgrObject = malloc_link_mgr(self)
        self.theSessionMgrObject = malloc_session_mgr(self)
        self.theClusterMgrObject = malloc_cluster_mgr(self)
        self.theSwitchObject = malloc_switch(self)

    def className(self):
        return "FibreClass"

    def phwangObject(self):
        return self.thePhwangObject

    def linkMgrObject(self):
        return self.theLinkMgrObject

    def sessionMgrObject(self):
        return self.theSessionMgrObject

    def clusterMgrObject(self):
        return self.theClusterMgrObject

    def switchObject(self):
        return self.theSwitchObject

    def utilObject(self):
        return self.phwangObject().utilObject()

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.phwangObject().logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.phwangObject().abend(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

