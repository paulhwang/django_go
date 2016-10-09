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
        self.goObject().portObject().forNow("03071004")
        self.goObject().portObject().forNow("03082005")
        self.goObject().portObject().forNow("03091006")
        self.goObject().portObject().forNow("03102007")
        self.goObject().portObject().forNow("03111008")
        self.goObject().portObject().forNow("03122009")
        self.goObject().portObject().forNow("03131010")
        self.goObject().portObject().forNow("03142011")
        self.goObject().portObject().forNow("03041012")
        self.goObject().portObject().forNow("03152013")

        self.goObject().portObject().forNow("04081014")
        self.goObject().portObject().forNow("04092015")
        self.goObject().portObject().forNow("04101016")
        self.goObject().portObject().forNow("04112017")
        self.goObject().portObject().forNow("04121018")
        self.goObject().portObject().forNow("04132019")

        self.goObject().portObject().forNow("11101020")
        self.goObject().portObject().forNow("16152021")
        self.goObject().portObject().forNow("11121022")
        self.goObject().portObject().forNow("16132023")
        self.goObject().portObject().forNow("11111024")
        self.goObject().portObject().forNow("16142025")

        self.goObject().portObject().forNow("05091026")

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.util_folder.util.utilLogit(self.className() + "." + str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.util_folder.util.utilAbend(self.className() + "." + str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
