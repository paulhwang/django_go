import go_server.phwang_modules.util_modules.util
import go_server.phwang_modules.fabric_modules.fabric
import go_server.phwang_modules.port_modules.port

def malloc():
    return PhwangClass()

def malloc_util(phwang_val):
    return go_server.phwang_modules.util_modules.util.malloc(phwang_val)

def malloc_farbric(phwang_val):
    return go_server.phwang_modules.fabric_modules.fabric.malloc(phwang_val)

def malloc_port(phwang_val):
    return go_server.phwang_modules.port_modules.port.malloc(phwang_val)

class PhwangClass(object):
    def __init__(self):
        self.theUtilObject = malloc_util(self)
        self.theFarbricObject = malloc_farbric(self)
        self.thePortObject = malloc_port(self)
        #self.debug(True, "init__", "")

    def className(self):
        return "PhwangClass"

    def utilObject(self):
        return self.theUtilObject

    def farbricObject(self):
        return self.theFarbricObject

    def portObject(self):
        return self.thePortObject

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
        go_server.phwang_modules.util_modules.util.utilLogit("GO:" + str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.util.utilAbend("GO:" + str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def LOG_IT(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.util.utilLogit(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def ABEND(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.util.utilAbend(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
