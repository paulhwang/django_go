import go_server.project_modules.port_modules.ajax

def malloc(root_val):
    return PortClass(root_val)

def malloc_ajax(port_val):
    return go_server.project_modules.port_modules.ajax.malloc(port_val)

class PortClass(object):
    def __init__(self, root_val):
        self.theRootObject = root_val
        self.theAjaxObject = malloc_ajax(self)

    def className(self):
        return "PortClass"

    def rootObject(self):
        return self.theRootObject

    def portObject(self):
        return self.thePortObject
