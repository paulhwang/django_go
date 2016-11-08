def malloc(session_mgr_val, session_id_val):
    return SessionClass(session_mgr_val, session_id_val)

class SessionClass(object):
    def __init__(self, session_mgr_val, session_id_val):
        self.theSessionMgrObject = session_mgr_val;
        self.resetIt(session_mgr_val, session_id_val)

    def objectName(self):
        return "SessionClass"

    def sessionMgrObject(self):
        return self.theSessionMgrObject

    def clusterObject(self):
        return self.theClusterObject

    def setClusterObject(self, val):
        self.theClusterObject = val

    def fabricObject(self):
        return self.sessionMgrObject().fabricObject()

    def utilObject(self):
        return self.sessionMgrObject().utilObject()

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

    def prev(self):
        return self.thePrev

    def setPrev(self, val):
        self.thePrev = val

    def next(self):
        return self.theNext

    def setNext(self, val):
        self.theNext = val

    def resetIt(self, session_mgr_val, session_id_val):
        self.theSessionMgrObject = session_mgr_val
        self.theSessionId = session_id_val
        self.theHisSession = None
        self.up_seq = 0
        self.down_seq = 0
        self.theReceiveQueue = self.utilObject().mallocQueue()
        self.theTransmitQueue = self.utilObject().mallocQueue()
        self.theReceiveRing = self.utilObject().mallocRing()
        self.thePrev = None
        self.theNext = None

    def enqueueTransmitData(self, data_val):
        self.debug(True, "enqueueTransmitData", data_val)
        self.transmitQueue().enQueue(data_val)

    def dequeueTransmitData(self):
        data = self.transmitQueue().deQueue()
        self.debug(False, "dequeueTransmitData", data)
        return data

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fabricObject().logit(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fabricObject().abend(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)