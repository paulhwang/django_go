import go_server.phwang_modules.farbric_modules.session

def malloc(link_val):
    return SessionMgrClass(link_val)

def malloc_session(session_mgr_val, session_id_val):
    return go_server.phwang_modules.farbric_modules.session.malloc(session_mgr_val, session_id_val)

class SessionMgrClass(object):
    def __init__(self, link_val):
        self.theLinkObject = link_val
        self.theSessionQueue = self.utilObject().mallocQueue()
        self.thePreSessionQueue = self.utilObject().mallocQueue()
        self.thePoolQueue = self.utilObject().mallocQueue()
        self.theGlobalSessionId = 1000

    def sessionModuleMalloc(self, session_id_val):
        return malloc_session(self, session_id_val)

    def objectName(self):
        return "SessionMgrClass"

    def linkObject(self):
        return self.theLinkObject

    def linkMgrObject(self):
        return self.linkObject().linkMgrObject()

    def fabricObject(self):
        return self.linkMgrObject().fabricObject()

    def phwangObject(self):
        return self.fabricObject().phwangObject()

    def clusterMgrObject(self):
        return self.fabricObject().clusterMgrObject()

    def utilObject(self):
        return self.phwangObject().utilObject()

    def sessionQueue(self):
        return self.theSessionQueue;

    def preSessionQueue(self):
        return self.thePreSessionQueue;

    def globalSessionId(self):
        return self.theGlobalSessionId;

    def incrementGlobalSessionId(self):
        self.theGlobalSessionId += 1

    def searchSessionBySessionId(self, session_id_val):
        return self.sessionQueue().searchIt(compareSessionId, session_id_val, None, None)

    def searchSession(self, my_name_val, his_name_val, session_id_val):
        return self.sessionQueue().searchIt(compareSessionData, my_name_val, his_name_val, session_id_val)

    def searchAndCreate(self, my_name_val, his_name_val, session_id_val):
        session = self.searchSession(my_name_val, his_name_val, session_id_val)
        if not session:
            cluster = self.clusterMgrObject().mallocCluster("go")
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

    def mallocSession(self):
        session = self.sessionModuleMalloc(self.globalSessionId())
        self.incrementGlobalSessionId()
        self.sessionQueue().enQueue(session)
        return session

    #def freeSession(self, session_val):

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.farbricObject().logit(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.farbricObject().abend(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

def compareSessionData(session_val, my_name_val, his_name_val, session_id_val):
    if my_name_val != session_val.myName():
        return False
    if his_name_val != session_val.hisName():
        return False
    if (session_id_val == session_val.sessionId()) or (session_id_val == 0):
        return True
    return False

def compareSessionId(session_val, session_id_val, dummy_val3, dummy_val4):
    return session_id_val == session_val.sessionId()

