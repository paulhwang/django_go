import go_server.phwang_modules.go_modules.go_root
import go_server.phwang_modules.fabric_modules.imports

def process_ajax_input(request_val):
    return the_root_object.ajaxObject().processInput(request_val)

class RootClass(object):
    def __init__(self):
        self.theImportObject = go_server.phwang_modules.fabric_modules.imports.malloc(self)
        self.theBaseObject = self.importObject().importBase().malloc(self)
        self.theLinkMgrObject = self.importObject().importListMgr().malloc_mgr(self, 0)
        self.theClusterBaseObject = self.importObject().importClusterBase().malloc(self)
        self.theClusterMgrObject = self.importObject().importListMgr().malloc_mgr(self, 0)
        self.theSwitchObject = self.importObject().importSwitch().malloc(self)
        self.theAjaxObject = self.importObject().importAjax().malloc(self)
        self.debug(True, "init__", "")

    def objectName(self):
        return "RootClass"

    def baseObject(self):
        return self.theBaseObject

    def linkMgrObject(self):
        return self.theLinkMgrObject

    def importObject(self):
        return self.theImportObject

    def clusterBaseObject(self):
        return self.theClusterBaseObject

    def clusterMgrObject(self):
        return self.theClusterMgrObject

    def switchObject(self):
        return self.theSwitchObject

    def ajaxObject(self):
        return self.theAjaxObject

    def topicMallocBase(self):
        return go_server.phwang_modules.go_modules.go_root.malloc_base()

    def topicReceiveData(self, base_id_val, data_val):
        go_server.phwang_modules.go_modules.go_root.receive_data(base_id_val, data_val)

    def topicTransmitData(self, base_id_val):
        return go_server.phwang_modules.go_modules.go_root.transmit_data(base_id_val)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def LOG_IT(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.logit.utilLogit(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def ABEND(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.logit.utilAbend(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

the_root_object = RootClass()
