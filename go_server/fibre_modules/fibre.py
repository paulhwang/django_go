import go_server.fibre_modules.link_mgr
import go_server.fibre_modules.session_mgr
import go_server.fibre_modules.cluster_mgr

def malloc(root_val):
    return FibreClass(root_val)

def malloc_link_mgr(root_val):
    return go_server.fibre_modules.link_mgr.malloc(root_val)

def malloc_session_mgr(root_val):
    return go_server.fibre_modules.session_mgr.malloc(root_val)

def malloc_cluster_mgr(root_val):
    return go_server.fibre_modules.cluster_mgr.malloc(root_val)

class FibreClass(object):
    def __init__(self, root_val):
        self.theRootObject = root_val
        self.theLinkMgrObject = malloc_link_mgr(self)
        self.theSessionMgrObject = malloc_session_mgr(self)
        self.theClusterMgrObject = malloc_cluster_mgr(self)

    def className(self):
        return "FibreClass"

    def fibreObject(self):
        return theFibreObject

    def linkMgrObject(self):
        return theLinkMgrObject

    def sessionMgrObject(self):
        return theSessionMgrObject
