import go_server.phwang_modules.util_modules.logit
import go_server.phwang_modules.util_modules.list_mgr
import go_server.phwang_modules.util_modules.queue
import go_server.phwang_modules.util_modules.ring

def malloc(root_object_val):
    return ImportObject(root_object_val)

class ImportObject (object):
    def __init__(self, root_object_val):
        self.theRootObject = root_object_val

    def rootObject(self):
        return self.theRootObject

    def importListMgr(self):
        return go_server.phwang_modules.util_modules.list_mgr

    def importLogit(self):
        return go_server.phwang_modules.util_modules.logit

    def mallocQueue(self):
        return go_server.phwang_modules.util_modules.queue.malloc(self.rootObject())

    def mallocRing(self):
        return go_server.phwang_modules.util_modules.ring.malloc(self.rootObject())
