import go_server.util_folder.util
import go_server.fibre_folder.fibre
import go_server.go_folder.go

def malloc():
    return RootClass()

def malloc_fibre(root_val):
    return go_server.fibre_folder.fibre.malloc(root_val)

def malloc_go(root_val):
    return go_server.go_folder.go.malloc(root_val)

class RootClass(object):
    def __init__(self):
        self.theFibreObject = malloc_fibre(self)
        self.theGoObject = malloc_go(self)

    def className(self):
        return "RootClass"

    def fibreObject(self):
        return self.theFibreObject

    def goObject(self):
        return self.theGoObject

    def test(self):
        self.goObject().portObject().forNow("03051000")
        self.goObject().portObject().forNow("03062001")

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.util_folder.util.utilLogit(self.className() + "." + str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.util_folder.util.utilAbend(self.className() + "." + str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
