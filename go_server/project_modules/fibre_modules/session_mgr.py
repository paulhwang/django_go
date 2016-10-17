def malloc(fibre_val):
    return SessionMgrClass(fibre_val)

class SessionMgrClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val
        self.theSessionQueue = self.utilObject().mallocQueue()
        self.thePreSessionQueue = self.utilObject().mallocQueue()
        self.theGlobalSessionId = 1000
        self.thePoolHead = 0
        self.thePoolSize = 0

    def className(self):
        return "SessionMgrClass"

    def fibreObject(self):
        return self.theFibreObject

    def rootObject(self):
        return self.fibreObject().rootObject()

    def utilObject(self):
        return self.rootObject().utilObject()

    def sessionQueue(self):
        return self.theSessionQueue;

    def preSessionQueue(self):
        return self.thePreSessionQueue;

    def globalSessionId(self):
        return self.theGlobalSessionId;

    def poolHead(self):
        return self.thePoolHead

    def setPoolHead(self, val):
        self.thePoolHead = val

    def poolSize(self):
        return self.thePoolSize

    def incrementPoolSize(self):
        self.thePoolSize += 1

    def decrementPoolSize(self):
        self.thePoolSize -= 1

    def searchSession(self, my_name_val, his_name_val, session_id_val):
        return self.sessionQueue().searchIt(compareSessionData, my_name_val, his_name_val, session_id_val)

    def searchAndCreate(self, my_name_val, his_name_val, session_id_val):
        session = self.searchSession(my_name_val, his_name_val, session_id_val)
        if not session:
            cluster = self.clusterModuleMalloc()
            session = self.mallocSession(my_name_val, his_name_val, cluster)
            self.sessionQueue().enQueue(session)

            if my_name_val == his_name_val:
                session.setHisName(his_name_val)
                session.setHisSession(session)
            else:
                his_session = self.mallocSession(his_name_val, my_name_val, cluster)
                session.setHisSession(his_session)
                his_session.setHisSession(session)
                self.sessionQueue().enQueue(his_session)
        return session

    def mallocSession(self, my_name_val, his_name_val, cluster_val):
        entry = self.poolQueue().deQueue();
        if not entry:
            entry = self.sessionModuleMalloc(self, my_name_val, his_name_val, self.globalSessionId(), cluster_val)
        else:
            entry.resetIt(my_name_val, his_name_val, self.globalSessionId(), cluster_val)
        self.incrementGlobalSessionId()
        return entry

    def freeSession(self, session_val):
        self.poolQueue().enQueue(link_val)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

def compareSessionData(session_val, my_name_val, his_name_val, session_id_val):
    if my_name_val != session_val.myName():
        return False
    if his_name_val != session_val.hisName():
        return False
    if (session_id_val == session_val.sessionId()) or (session_id_val == 0):
        return True
    return False

