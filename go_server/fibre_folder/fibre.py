import go_server.fibre_folder.link_mgr

def malloc(root_val):
    return FibreClass(root_val)

class FibreClass(object):
    def __init__(self, root_val):
        self.theRootObject = root_val
        self.theLinkMgrObject = go_server.fibre_folder.link_mgr.malloc(self)

    def className(self):
        return "FibreClass"

    def fibreObject(self):
        return theFibreObject

    def linkMgrObject(self):
        return theLinkMgrObject