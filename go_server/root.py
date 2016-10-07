import go_server.fibre_folder.fibre
import go_server.go_folder.go

def malloc():
	return RootClass()

class RootClass(object):
    def __init__(self):
        self.theFibreObject = go_server.fibre_folder.fibre.malloc(self)
        self.theGoObject = go_server.go_folder.go.malloc(self)

    def className(self):
        return "RootClass"

    def fibreObject(self):
        return self.theFibreObject

    def goObject(self):
        return self.theGoObject

