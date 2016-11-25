import go_server.phwang_modules.go_modules.go_import

def malloc_base():
    return the_go_root_object.mallocBase()

def receive_data(base_id_val, data_val):
    the_go_root_object.receiveData(base_id_val, data_val)

def transmit_data(base_id_val):
    return the_go_root_object.transmitData(base_id_val)

class GoRootClass(object):
    def __init__(self):
        self.theImportObject = go_server.phwang_modules.go_modules.go_import.malloc(self)
        self.theBaseMgrObject = self.importObject().importListMgr().malloc_mgr(self, 100)
        self.debug(True, "init__", "")

    def objectName(self):
        return "GoRootClass"

    def importObject(self):
        return self.theImportObject

    def baseMgrObject(self):
        return self.theBaseMgrObject

    def mallocQueue(self):
        return go_server.phwang_modules.util_modules.queue.malloc(self)

    def mallocRing(self):
        return go_server.phwang_modules.util_modules.ring.malloc(self)

    def mallocBase(self):
        base = self.importObject().importBase().malloc(self, self.baseMgrObject().allocId())
        self.baseMgrObject().insertEntry(base)
        self.debug(False, "mallocBase", "baseId=%d", base.baseId())
        return base.baseId()

    def receiveData(self, base_id_val, data_val):
        self.debug(False, "receiveData", "data=%s", data_val)
        base = self.baseMgrObject().searchId(base_id_val)
        if not base:
            return
        base.portObject().receiveStringData(data_val)

    def transmitData(self, base_id_val):
        base = self.baseMgrObject().searchId(base_id_val)
        if not base:
            return None
        return base.portObject().dequeueTransmitData()

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def LOG_IT(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.importObject().importLogit().utilLogit(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def ABEND(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.importObject().importLogit().utilAbend(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

the_go_root_object = GoRootClass()

