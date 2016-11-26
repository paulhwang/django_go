import go_server.phwang_modules.util_modules.logit
import go_server.phwang_modules.util_modules.list_mgr
import go_server.phwang_modules.util_modules.queue
import go_server.phwang_modules.util_modules.ring
import go_server.phwang_modules.fabric_modules.base
import go_server.phwang_modules.fabric_modules.link_mgr
import go_server.phwang_modules.fabric_modules.link
import go_server.phwang_modules.fabric_modules.cluster_mgr
import go_server.phwang_modules.fabric_modules.cluster
import go_server.phwang_modules.fabric_modules.switch
import go_server.phwang_modules.fabric_modules.session
import go_server.phwang_modules.fabric_modules.ajax
import go_server.phwang_modules.fabric_modules.imports

def malloc(root_object_val):
    return ImportObject(root_object_val)

class ImportObject (object):
    def __init__(self, root_object_val):
        self.theRootObject = root_object_val

    def rootObject(self):
        return self.theRootObject

    def importBase(self):
        return go_server.phwang_modules.fabric_modules.base

    def importSwitch(self):
        return go_server.phwang_modules.fabric_modules.switch

    def importAjax(self):
        return go_server.phwang_modules.fabric_modules.ajax

    def importLinkMgr(self):
        return go_server.phwang_modules.fabric_modules.link_mgr

    def importLink(self):
        return go_server.phwang_modules.fabric_modules.link

    def importSession(self):
        return go_server.phwang_modules.fabric_modules.session

    def importClusterMgr(self):
        return go_server.phwang_modules.fabric_modules.cluster_mgr

    def importCluster(self):
        return go_server.phwang_modules.fabric_modules.cluster

    def importListMgr(self):
        return go_server.phwang_modules.util_modules.list_mgr

    def importLogit(self):
        return go_server.phwang_modules.util_modules.logit

    def mallocQueue(self):
        return go_server.phwang_modules.util_modules.queue.malloc(self.rootObject())

    def mallocRing(self):
        return go_server.phwang_modules.util_modules.ring.malloc(self.rootObject())
