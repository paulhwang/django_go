import go_server.project_modules.go_modules.go
import json

def malloc(cluster_mgr_val):
    return ClusterClass(cluster_mgr_val)

class ClusterClass(object):
    def __init__(self, cluster_mgr_val):
        self.theClusterMgrObject = cluster_mgr_val;
        self.theSessionArray = [2]
        self.theSessionArrayLength = 0
        self.theGoObject = self.goObjectMalloc()
        self.theReceiveQueue = self.utilObject().mallocQueue()
        self.theTransmitQueue = self.utilObject().mallocQueue()
        self.theNext = None

    def goObjectMalloc(self):
        return go_server.project_modules.go_modules.go.malloc(self)

    def className(self):
        return "ClusterClass"

    def clusterMgrObject(self):
        return self.theClusterMgrObject

    def goObject(self):
        return self.theGoObject

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

    def receiveQueue(self):
        return self.theReceiveQueue

    def transmitQueue(self):
        return self.theTransmitQueue

    def addAdditionalSession(self, session_val):
        self.theSessionArray[self.sessionArrayLength()] = session_val
        self.incrementSessionArrayLength()

    def enqueueReceiveData(self, data_val):
        self.debug(True, "enqueueReceiveData", data_val)
        self.receiveQueue().enQueue(data_val)

    def dequeueReceiveData(self):
        data = self.receiveQueue().deQueue()
        self.debug(True, "dequeueReceiveData", data)
        return data

    def processSetupTopicData(self, json_data_val):
        self.debug(True, "processSetupTopicData", "data=%s", json_data_val)
        topic_data = json.loads(json_data_val)
        if topic_data.get("command") == "config":
            self.goObject().configObject().createConfig(topic_data.get("data"))

    def processReceiveData(self):
        while True:
            data = self.dequeueReceiveData()
            if not data:
                return
            self.receiveStringData(data)

    def enqueAndPocessReceiveData(self, data_val):
        self.debug(True, "enqueAndPocessReceiveData", data_val)
        self.enqueueReceiveData(data_val)
        self.processReceiveData()

    def receiveStringData(self, str_val):
        self.goObject().portObject().receiveStringData(str_val)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.clusterMgrObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.clusterMgrObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
