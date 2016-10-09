import go_server.project_modules.util_modules.util
import go_server.project_modules.fibre_modules.fibre
import go_server.project_modules.go_modules.go

def malloc():
    return RootClass()

def malloc_fibre(root_val):
    return go_server.project_modules.fibre_modules.fibre.malloc(root_val)

def malloc_go(root_val):
    return go_server.project_modules.go_modules.go.malloc(root_val)

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
        self.goObject().portObject().receiveStringData("03062001")

    def test1(self):
        self.goObject().portObject().receiveStringData("03051000")
        self.goObject().portObject().receiveStringData("03062001")
        self.goObject().portObject().receiveStringData("03071004")
        self.goObject().portObject().receiveStringData("03082005")
        self.goObject().portObject().receiveStringData("03091006")
        self.goObject().portObject().receiveStringData("03102007")
        self.goObject().portObject().receiveStringData("03111008")
        self.goObject().portObject().receiveStringData("03122009")
        self.goObject().portObject().receiveStringData("03131010")
        self.goObject().portObject().receiveStringData("03142011")
        self.goObject().portObject().receiveStringData("03041012")
        self.goObject().portObject().receiveStringData("03152013")

        self.goObject().portObject().receiveStringData("04081014")
        self.goObject().portObject().receiveStringData("04092015")
        self.goObject().portObject().receiveStringData("04101016")
        self.goObject().portObject().receiveStringData("04112017")
        self.goObject().portObject().receiveStringData("04121018")
        self.goObject().portObject().receiveStringData("04132019")

        self.goObject().portObject().receiveStringData("11101020")
        self.goObject().portObject().receiveStringData("16152021")
        self.goObject().portObject().receiveStringData("11121022")
        self.goObject().portObject().receiveStringData("16132023")
        self.goObject().portObject().receiveStringData("11111024")
        self.goObject().portObject().receiveStringData("16142025")

        self.goObject().portObject().receiveStringData("05091026")

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.project_modules.util_modules.util.utilLogit(self.className() + "." + str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.project_modules.util_modules.util.utilAbend(self.className() + "." + str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
