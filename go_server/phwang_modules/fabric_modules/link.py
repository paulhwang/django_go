import threading
import json

def malloc(root_object_val, my_name_val, link_id_val):
    return LinkClass(root_object_val, my_name_val, link_id_val)

class LinkClass(object):
    def __init__(self, root_object_val, my_name_val, link_id_val):
        self.theRootObject = root_object_val;
        self.theJointObject = self.importObject().importListMgr().malloc_joint(link_id_val)
        self.theMyName = my_name_val
        self.theLinkId = link_id_val
        self.theGlobalSessionId = 1000
        self.theKeepAliveTimer = None
        self.thePrev = None
        self.theNext = None
        self.up_seq = 0
        self.down_seq = 0
        self.theReceiveQueue = self.importObject().mallocQueue()
        self.thePendingSessionSetupQueue = self.importObject().mallocQueue()
        self.theNameListChanged = True
        self.theSessionMgrObject = self.importObject().importListMgr().malloc_mgr(self, 100)
        self.debug(True, "init__", "")

    def linkTimeoutInterval(self):
        return 30.0

    def objectName(self):
        return "LinkClass"

    def rootObject(self):
        return self.theRootObject

    def importObject(self):
        return self.rootObject().importObject()

    def jointObject(self):
        return self.theJointObject

    def sessionMgrObject(self):
        return self.theSessionMgrObject

    def utilObject(self):
        return self.linkMgrObject().utilObject()

    def linkId(self):
        return self.theLinkId

    def setLinkId(self, val):
        self.theLinkId = val

    def myName(self):
        return self.theMyName

    def setMyName(self, val):
        self.theMyName = val

    def globalSessionId(self):
        return self.theGlobalSessionId

    def incrementGlobalSessionId(self):
        self.theGlobalSessionId += 1

    def keepAliveTimer(self):
        return self.theKeepAliveTimer

    def setKeepAliveTimer(self, val):
        self.theKeepAliveTimer = val

    def receiveQueue(self):
        return self.theReceiveQueue

    def receiveRing(self):
        return self.theReceiveRing

    def pendingSessionSetupQueue(self):
        return self.thePendingSessionSetupQueue

    def prev(self):
        return self.thePrev

    def setPrev(self, val):
        self.thePrev = val

    def next(self):
        return self.theNext

    def setNext(self, val):
        self.theNext = val

    def nameListChanged(self):
        return self.theNameListChanged

    def setNameListChanged(self):
        self.theNameListChanged = True

    def clearNameListChanged(self):
        self.theNameListChanged = False

    def resetKeepAliveTimer(self):
        self.debug(False, "resetKeepAliveTimer", "my_name=%s link_id=%i", self.myName(), self.linkId())
        self.setKeepAliveTimer(self.resetTimeout())

    def resetTimeout(self):
        if self.keepAliveTimer():
            self.keepAliveTimer().cancel()

        t = threading.Timer(self.linkTimeoutInterval(), timeoutFunction_, [self])
        t.start()
        return t

    def searchSessionBySessionId(self, session_id_val):
        return self.sessionMgrObject().searchId(session_id_val)

    def mallocSession(self):
        session = self.importObject().importSession().malloc(self, self.globalSessionId())
        self.incrementGlobalSessionId()
        self.sessionMgrObject().insertEntry(session)
        return session

    def getPendingSessionData(self):
        data = []
        i = 0
        session = self.importObject().importListMgr().head(self.sessionMgrObject())
        while session:
            if session.transmitQueue().size() > 0:
                data.append(session.sessionId())
                i += 1
            session = self.importObject().importListMgr().next(session)
        if i == 0:
            return None
        else:
            return data

    def getPendingSessionSetup(self):
        return self.pendingSessionSetupQueue().deQueue();

    def setPendingSessionSetup (self, session_val, topic_data_val):
        self.pendingSessionSetupQueue().enQueue(json.dumps({"session_id": session_val.sessionId(),
                                                            "topic_data": topic_data_val
                                                            }))

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

def timeoutFunction_(link_val):
    link_val.debug(True, "timeoutFunction_(***timeout occurs)", "link_id=%i", link_val.linkId())
    link_val.keepAliveTimer().cancel()
    link_val.linkMgrObject().freeLink(link_val)
