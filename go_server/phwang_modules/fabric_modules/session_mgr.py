def malloc(link_val):
    return SessionMgrClass(link_val)

class SessionMgrClass(object):
    def __init__(self, link_val):
        self.theLinkObject = link_val
        self.theHead = None
        self.theTail = None
        self.theSize = 0
        self.theGlobalSessionId = 1000
        self.debug(True, "init__", "")

    def sessionModuleMalloc(self, session_id_val):
        return self.rootObject().importObject().importSession().malloc(self, session_id_val)

    def objectName(self):
        return "SessionMgrClass"

    def linkObject(self):
        return self.theLinkObject

    def fabricObject(self):
        return self.rootObject().fabricObject()

    def rootObject(self):
        return self.linkObject().rootObject()

    def clusterMgrObject(self):
        return self.fabricObject().clusterMgrObject()

    def utilObject(self):
        return self.rootObject().utilObject()

    def globalSessionId(self):
        return self.theGlobalSessionId

    def incrementGlobalSessionId(self):
        self.theGlobalSessionId += 1

    def head(self):
        return self.theHead

    def setHead(self, val):
        self.theHead = val

    def tail(self):
        return self.theTail

    def setTail(self, val):
        self.theTail = val

    def size(self):
        return self.theSize

    def incrementSize(self):
        self.theSize += 1

    def decrementSize(self):
        self.theSize -= 1

    def mallocSession(self):
        session = self.sessionModuleMalloc(self.globalSessionId())
        self.incrementGlobalSessionId()
        self.insertSessionToList(session)
        return session

    def freeSession(self, session_val):
        self.deleteSessionFromList(session_val)

    def insertSessionToList(self, session_val):
        if not session_val:
            self.abend("enQueue", "null session_val")
            return

        self.abendIt()

        self.incrementSize()
        if not self.head():
            session_val.setPrev(None)
            session_val.setNext(None)
            self.setHead(session_val)
            self.setTail(session_val)
        else:
            self.tail().setNext(session_val)
            session_val.setPrev(self.tail())
            session_val.setNext(None)
            self.setTail(session_val)
        self.abendIt()

    def deleteSessionFromList(self, session_val):
        if self.size() <= 0:
            self.abend("deleteSessionFromList", "size=%i", self.size())
            return
        if not self.sessionExistInTheList(session_val):
            self.abend("deleteSessionFromList", "sessionExistInTheList is false")
            return

        self.abendIt()
        if session_val.prev():
            session_val.prev().setNext(session_val.next())
        else:
            self.setHead(session_val.next())
        if session_val.next():
            session_val.next().setPrev(session_val.prev())
        else:
            self.setTail(session_val.prev())
        self.decrementSize()
        self.abendIt()

    def searchSessionBySessionId(self, session_id_val):
        session = self.head()
        while session:
            if session.sessionId() == session_id_val:
                return session
            session = session.next()
        return None

    def sessionExistInTheList(self, session_val):
        session = self.head()
        while session:
            if session == session_val:
                return True
            session = session.next()
        return False

    def getPendingSessionData(self):
        data = []
        i = 0
        session = self.head()
        while session:
            if session.transmitQueue().size() > 0:
                data.append(session.sessionId())
                i += 1
            session = session.next();
        if i == 0:
            return None
        else:
            return data

    def abendIt(self):
        i = 0;
        session = self.head()
        while session:
            session = session.next()
            i += 1
        if i != self.size():
            self.abend("abendIt", "head: size=%i i=%i", self.size(), i)

        i = 0
        session = self.tail()
        while session:
            session = session.prev()
            i += 1
        if i != self.size():
            self.abend("abendIt", "tail: size=%i i=%i", self.size(), i)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
