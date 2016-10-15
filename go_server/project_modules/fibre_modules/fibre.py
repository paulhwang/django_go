import go_server.project_modules.fibre_modules.link_mgr
import go_server.project_modules.fibre_modules.session_mgr
import go_server.project_modules.fibre_modules.cluster_mgr
import go_server.project_modules.fibre_modules.dispatch

def malloc(root_val):
    return FibreClass(root_val)

def malloc_link_mgr(root_val):
    return go_server.project_modules.fibre_modules.link_mgr.malloc(root_val)

def malloc_session_mgr(root_val):
    return go_server.project_modules.fibre_modules.session_mgr.malloc(root_val)

def malloc_cluster_mgr(root_val):
    return go_server.project_modules.fibre_modules.cluster_mgr.malloc(root_val)

def malloc_dispatch(root_val):
    return go_server.project_modules.fibre_modules.dispatch.malloc(root_val)

class FibreClass(object):
    def __init__(self, root_val):
        self.theRootObject = root_val
        self.theLinkMgrObject = malloc_link_mgr(self)
        self.theSessionMgrObject = malloc_session_mgr(self)
        self.theClusterMgrObject = malloc_cluster_mgr(self)
        self.theDispatchObject = malloc_dispatch(self)

    def className(self):
        return "FibreClass"

    def fibreObject(self):
        return self.theFibreObject

    def linkMgrObject(self):
        return self.theLinkMgrObject

    def sessionMgrObject(self):
        return self.theSessionMgrObject

    def dispatchObject(self):
        return self.theDispatchObject

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

