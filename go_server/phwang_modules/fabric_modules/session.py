def malloc(link_object_val, session_id_val):
    return SessionClass(link_object_val, session_id_val)

class SessionClass(object):
    def __init__(self, link_object_val, session_id_val):
        self.theLinkObject = link_object_val;
        self.theJointObject = self.rootObject().importObject().importListMgr().malloc_joint(session_id_val)
        self.resetIt(link_object_val, session_id_val)
        self.debug(True, "init__", "")

    def objectName(self):
        return "SessionClass"

    def linkObject(self):
        return self.theLinkObject

    def jointObject(self):
        return self.theJointObject

    def clusterObject(self):
        return self.theClusterObject

    def setClusterObject(self, val):
        self.theClusterObject = val

    def fabricObject(self):
        return self.linkObject().fabricObject()

    def rootObject(self):
        return self.linkObject().rootObject()

    def utilObject(self):
        return self.linkObject().utilObject()

    def sessionId(self):
        return self.theSessionId

    def setSessionId(self, val):
        self.theSessionId = val

    def myName(self):
        return self.theMyName

    def setMyName(val):
        self.theMyName = val

    def hisName(self):
        return self.theHisName

    def setHisName(self, val):
        self.theHisName = val
 
    def hisSession(self):
        return self.theHisSession;

    def setHisSession(self, val):
        self.theHisSession = val;

    def receiveQueue(self):
        return self.theReceiveQueue;

    def transmitQueue(self):
        return self.theTransmitQueue;

    def receiveRing(self):
        return self.theReceiveRing;

    def resetIt(self, link_object_val, session_id_val):
        self.theLinkObject = link_object_val
        self.theSessionId = session_id_val
        self.theHisSession = None
        self.up_seq = 0
        self.down_seq = 0
        self.theReceiveQueue = self.rootObject().importObject().mallocQueue()
        self.theTransmitQueue = self.rootObject().importObject().mallocQueue()

    def enqueueTransmitData(self, data_val):
        self.debug(False, "enqueueTransmitData", data_val)
        self.transmitQueue().enQueue(data_val)

    def dequeueTransmitData(self):
        data = self.transmitQueue().deQueue()
        self.debug(False, "dequeueTransmitData", data)
        return data

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
