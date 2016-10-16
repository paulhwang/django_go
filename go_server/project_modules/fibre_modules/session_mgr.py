def malloc(fibre_val):
    return SessionMgrClass(fibre_val)

class SessionMgrClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val
        self.theSessionQueue = self.utilObject().mallocQueue()
        self.thePreSessionQueue = self.utilObject().mallocQueue()
        self.theGlobalSessionId = 1000
        self.thePoolHead = 0
        self.thePoolSize = 0

    def className(self):
        return "SessionMgrClass"

    def fibreObject(self):
        return self.theFibreObject

    def rootObject(self):
        return self.fibreObject().rootObject()

    def utilObject(self):
        return self.rootObject().utilObject()

    def sessionQueue(self):
        return self.theSessionQueue;

    def preSessionQueue(self):
        return self.thePreSessionQueue;

    def globalSessionId(self):
        return self.theGlobalSessionId;

    def poolHead(self):
        return self.thePoolHead

    def setPoolHead(self, val):
        self.thePoolHead = val

    def poolSize(self):
        return self.thePoolSize

    def incrementPoolSize(self):
        self.thePoolSize += 1

    def decrementPoolSize(self):
        self.thePoolSize -= 1

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)


