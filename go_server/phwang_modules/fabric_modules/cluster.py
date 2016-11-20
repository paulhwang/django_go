import go_server.phwang_modules.go_modules.go
import json

def malloc(cluster_mgr_val, topic_data_val, session_val):
    return ClusterClass(cluster_mgr_val, topic_data_val, session_val)

class ClusterClass(object):
    def __init__(self, cluster_mgr_val, topic_data_val, session_val):
        self.theClusterMgrObject = cluster_mgr_val
        session_val.setClusterObject(self)
        self.theSessionArray = [None] * 2
        self.theSessionArray[0] = session_val
        self.theSessionArrayLength = 1
        self.theReceiveQueue = self.utilObject().mallocQueue()
        self.theTransmitQueue = self.utilObject().mallocQueue()
        self.theNext = None
        self.thePrev = None
        self.createTopic(topic_data_val)
        self.debug(True, "init__", "topic=%s", self.topicObject().objectName())

    def goObjectMalloc(self):
        return go_server.phwang_modules.go_modules.go.malloc(self)

    def objectName(self):
        return "ClusterClass"

    def clusterMgrObject(self):
        return self.theClusterMgrObject

    def fabricObject(self):
        return self.clusterMgrObject().fabricObject()

    def rootObject(self):
        return self.fabricObject().rootObject()

    def utilObject(self):
        return self.clusterMgrObject().utilObject()

    def topicObject(self):
        return self.theTopicObject

    def setTopicObject(self, val):
        self.theTopicObject = val

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

    def prev(self):
        return self.thePrev

    def setPrev(self, val):
        self.thePrev = val

    def next(self):
        return self.theNext

    def setNext(self, val):
        self.theNext = val

    def createTopic(self, data_val):
        self.debug(False, "createTopic", data_val)
        data = json.loads(data_val)
        if data.get("title") == "go":
            self.setTopicObject(self.goObjectMalloc())

    def addAdditionalSession(self, session_val):
        self.theSessionArray[self.sessionArrayLength()] = session_val
        self.incrementSessionArrayLength()

    def enqueueTransmitData(self, data_val):
        self.debug(False, "enqueueTransmitData", data_val)
        self.transmitQueue().enQueue(data_val)

    def dequeueTransmitData(self):
        data = self.transmitQueue().deQueue()
        if data:
            self.debug(False, "dequeueTransmitData", "data=%s", data)
        else:
            self.debug(False, "dequeueTransmitData", "queue is empty")
        return data

    def enqueueReceiveData(self, data_val):
        self.debug(False, "enqueueReceiveData", data_val)
        self.receiveQueue().enQueue(data_val)

    def dequeueReceiveData(self):
        data = self.receiveQueue().deQueue()
        if data:
            self.debug(False, "dequeueReceiveData", "data=%s", data)
        else:
            self.debug(False, "dequeueReceiveData", "queue is empty")
        return data

    def processTransmitData(self):
        while True:
            data = self.dequeueTransmitData()
            if not data:
                return
            i = 0
            while i < self.sessionArrayLength():
                self.sessionArray(i).enqueueTransmitData(data)
                i += 1

    def processSetupTopicData(self, json_data_val):
        self.debug(False, "processSetupTopicData", "data=%s", json_data_val)
        topic_data = json.loads(json_data_val)
        if topic_data.get("command") == "config":
            self.topicObject().configObject().createConfig(topic_data.get("data"))

    def processReceiveData(self):
        while True:
            data = self.dequeueReceiveData()
            if not data:
                return
            self.receiveStringData(data)

    def enqueAndPocessReceiveData(self, data_val):
        self.debug(False, "enqueAndPocessReceiveData", data_val)
        self.enqueueReceiveData(data_val)
        self.processReceiveData()

    def receiveStringData(self, str_val):
        self.topicObject().portObject().receiveStringData(str_val)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
