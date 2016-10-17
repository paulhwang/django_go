def malloc(session_mgr_val, my_name_val, his_name_val, session_id_val, cluster_val):
    return SessionClass(session_mgr_val, my_name_val, his_name_val, session_id_val, cluster_val)

class SessionClass(object):
    def __init__(self, session_mgr_val, my_name_val, his_name_val, session_id_val, cluster_val):
        self.theSessionMgrObject = session_mgr_val;
        self.resetIt(session_mgr_val, my_name_val, his_name_val, session_id_val, cluster_val)

    def className(self):
        return "SessionClass"

    def sessionMgrObject(self):
        return self.theSessionMgrObject

    def clusterObject(self):
        return self.theClusterObject

    def fibreObject(self):
        return self.sessionMgrObject().FibreObject()

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

    def resetIt(self, session_mgr_val, my_name_val, his_name_val, session_id_val, cluster_val):
        self.theSessionMgrObject = session_mgr_val
        self.theSessionId = session_id_val
        self.theMyName = my_name_val
        self.theHisName = his_name_val
        self.theHisSession = None
        self.up_seq = 0
        self.down_seq = 0
        self.theReceiveQueue = self.utilObject().mallocQueue()
        self.theTransmitQueue = self.utilObject().mallocQueue()
        self.theReceiveRing = self.utilObject().mallocRing()
        self.theClusterObject = cluster_val
        self.clusterObject().addAdditionalSession(self)

    def dequeueTransmitData(self):
        data = self.transmitQueue().deQueue()
        self.debug(False, "dequeueTransmitData", data)
        return data

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.sessionMgrObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.sessionMgrObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
