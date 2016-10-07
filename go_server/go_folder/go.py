import go_server.fibre_folder.link_mgr

def malloc(root_val):
    return GoClass(root_val)

class GoClass(object):
    def __init__(self, root_val):
        self.theRootObject = root_val
        self.theGoEngineObject = go_server.fibre_folder.link_mgr.malloc(self)

    def className(self):
        return "GoClass"

    def fibreObject(self):
        return theFibreObject

    def goEngineObject(self):
        return theGoEngineObject