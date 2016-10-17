import go_server.project_modules.go_modules.go

def malloc(cluster_mgr_val):
    return ClusterClass(cluster_mgr_val)

class ClusterClass(object):
    def __init__(self, cluster_mgr_val):
        self.theClusterMgrObject = cluster_mgr_val;
        self.theSessionArray = [2]
        self.theSessionArrayLength = 0
        self.theGoContainerObject = self.goObjectMalloc()
        self.theReceiveQueue = self.utilObject().mallocQueue()
        self.theTransmitQueue = self.utilObject().mallocQueue()
        self.theNext = None

    def goObjectMalloc(self):
        return go_server.project_modules.go_modules.go.malloc(self.rootObject())

    def className(self):
        return "ClusterClass"

    def clusterMgrObject(self):
        return self.theClusterMgrObject

    def fibreObject(self):
        return self.clusterMgrObject().fibreObject()

    def rootObject(self):
        return self.fibreObject().rootObject()

    def utilObject(self):
        return self.clusterMgrObject().utilObject()

    def sessionArray(self, index_val):
        return self.theSessionArray[index_val]

    def sessionArrayLength(self):
        return self.theSessionArrayLength

    def incrementSessionArrayLength(self):
        self.theSessionArrayLength += 1

    def addAdditionalSession(self, session_val):
        self.theSessionArray[self.sessionArrayLength()] = session_val
        self.incrementSessionArrayLength()

    def processSetupTopicData(self, json_data_val):
        self.debug(True, "processSetupTopicData", "data=%s", json_data_val)
        json = JSON.parse(json_data_val)
        if json.command == "config":
            self.goContainerObject().configObject().createConfig(json.data)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.clusterMgrObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.clusterMgrObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
