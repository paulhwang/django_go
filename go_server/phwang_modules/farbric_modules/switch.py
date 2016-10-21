import json

def malloc(fabric_val):
    return SwitchClass(fabric_val)

class SwitchClass(object):
    def __init__(self, fabric_val):
        self.theFarbricObject = fabric_val
        self.initSwitchTable()

    def className(self):
        return "SwitchClass"

    def farbricObject(self):
        return self.theFarbricObject

    def linkMgrObject(self):
        return self.farbricObject().linkMgrObject()

    def sessionMgrObject(self):
        return self.farbricObject().sessionMgrObject()

    def initSwitchTable(self):
        self.switch_table = {
            "setup_link": self.setupLink,
            "get_link_data": self.getLinkData,
            "put_link_data": self.putLinkData,
            "get_name_list": self.getNameList,
            "setup_session": self.setupSession,
            "get_session_data": self.getSessionData,
            "put_session_data": self.putSessionData,
            "keep_alive": self.keepAlive,
        }

    def switchRequest(self, go_request):
        if not go_request:
            self.abend("switchRequest", "null go_request")
            return None

        self.debug(False, "switchRequest", "command=%s", go_request["command"])

        func = self.switch_table[go_request.get("command")]
        if func:
            return func(go_request)
        else:
            self.abend("switchRequest", "bad command=" + go_request.command)
            return None

    def setupLink(self, go_request):
        link = self.linkMgrObject().searchAndCreate(go_request.get("my_name"), 0)
        if not link:
            self.abend("setupLink", "null link")
            return None
        link.resetKeepAliveTimer()

        json_data = json.dumps({"link_id": link.linkId()});
        self.debug(False, "setupLink", "name=%s link_id=%i", go_request.get("my_name"), link.linkId())
        return json_data

    def getLinkObject(self, go_request):
        link = self.linkMgrObject().searchLink(go_request.get("my_name"), go_request.get("link_id"))
        if not link:
            self.abend("getLinkObject", "null link: link_id=%i my_name=%s", go_request.get("link_id"), go_request.get("my_name"))
            return None
        if link.linkId() == 0:
            self.abend("getLinkObject", "link_id = 0")
            return None

        link.resetKeepAliveTimer()
        return link

    def getLinkData(self, go_request):
        self.debug(False, "getLinkData", "link_id=%i my_name=%s ajax_id=%i", go_request.get("link_id"), go_request.get("my_name"), go_request.get("ajax_id"))

        link = self.getLinkObject(go_request)
        if not link:
            return None

        data = link.receiveQueue().deQueue()
        if data:
            self.debug(False, "getLinkData", "link_id=%i my_name=%s data={%s}", go_request.get("link_id"), go_request.get("my_name"), data)
        return json.dumps(data)

    def putLinkData(self, go_request):
        self.abend("putLinkData", "putLinkData is not implemented")
        return None

    def getNameList(self, go_request):
        link = self.getLinkObject(go_request)
        if not link:
            return None

        json_data = json.dumps(self.linkMgrObject().getNameList())
        self.debug(False, "getNameList", "link_id=%i my_name=%s data=%s", link.linkId(), go_request.get("my_name"), json_data)
        return json_data

    def setupSession (self, go_request):
        session = self.sessionMgrObject().searchSession(go_request.get("my_name"), go_request.get("his_name"), go_request.get("link_id"))
        if not session:
            session = self.sessionMgrObject().searchAndCreate(go_request.get("my_name"), go_request.get("his_name"), 0)
            if not session:
                res.send(self.jsonStingifyData(go_request.command, go_request.ajax_id, null))
                self.abend("setupSession", "null session")
                return None

        his_link = self.linkMgrObject().searchLink(go_request.get("his_name"), 0)
        if not his_link:
            res.send(self.jsonStingifyData(go_request.get("command"), go_request.get("ajax_id"), None))
            return None

        self.debug(True, "setupSession", "(%i:%i,%i) %s=>%s data=%s", go_request.get("link_id"), session.sessionId(), session.hisSession().sessionId(), go_request.get("my_name"), go_request.get("his_name"), go_request.get("data"))

        if go_request.get("data") != None:
            session.clusterObject().processSetupTopicData(go_request.get("data"))

        session_id_str = str(session.hisSession().sessionId())
        data = json.dumps({
                        "order": "setup_session",
                        "session_id": session_id_str,
                        "his_name": go_request.get("my_name"),
                        "my_name": go_request.get("his_name"),
                        "extra_data": go_request.get("data"),
                    });
        his_link.receiveQueue().enQueue(data);
        self.sessionMgrObject().preSessionQueue().enQueue(data)
        return self.setupSessionReply(session, go_request);

    def setupSessionReply(self, session_val, go_request):
        session_id_str = str(session_val.sessionId())
        data = json.dumps({
                        "session_id": session_id_str,
                        "extra_data": go_request.get("data"),
                    })
        self.debug(True, "setupSessionReply", "(%i,%i,%i) %s=>%s", go_request.get("link_id"), session_val.sessionId(), session_val.hisSession().sessionId(), go_request.get("my_name"), go_request.get("his_name"))
        return data

    def getSessionObject(self, go_request):
        link = self.getLinkObject(go_request)
        if not link:
            return None

        session = self.sessionMgrObject().searchSession(go_request.get("my_name"), go_request.get("his_name"), go_request.get("session_id"))
        if not session:
            self.abend("getSessionObject", "null session session_id=%s", go_request.get("session_id"))
            return None

        return session

    def getSessionData(self, go_request):
        self.debug(False, "getSessionData", "(%i:%i) %s=>%s", go_request.get("link_id"),  go_request.get("session_id"), go_request.get("my_name"), go_request.get("his_name"))

        session = self.getSessionObject(go_request)
        if not session:
            return None

        res_data = session.dequeueTransmitData()
        if not res_data:
            self.debug(False, "getSessionData", "no data")
            return None

        self.debug(False, "getSessionData", "ajax_id=%i", go_request.get("ajax_id"))
        self.debug(True, "getSessionData", "(%i,%i %s=>%s) {%s}", go_request.get("link_id"), go_request.get("session_id"), go_request.get("his_name"), go_request.get("my_name"), res_data)
        return res_data

    def putSessionData(self, go_request):
        #console.log(req.headers);
        #self.debug(True, "putSessionData ", "ajax_id=%i", go_request.get("ajax_id"))
        self.debug(True, "putSessionData ", "(%i,%i) %s=>%s (%s}", go_request.get("link_id"), go_request.get("session_id"), go_request.get("his_name"), go_request.get("my_name"), go_request.get("data"))

        session = self.getSessionObject(go_request)
        if not session:
            return None

        self.debug(True, "putSessionData", "(%i,%i) %s=>%s {%s} %i=>%i", go_request.get("link_id"), go_request.get("session_id"), go_request.get("my_name"), go_request.get("his_name"), go_request.get("data"), go_request.get("xmt_seq"), session.up_seq)

        if go_request.get("xmt_seq") == session.up_seq:
            session.clusterObject().enqueAndPocessReceiveData(go_request.get("data"))
            session.up_seq += 1
        else:
            if go_request.get("xmt_seq") < session.up_seq:
                if go_request.xmt_seq == 0:
                    session.clusterObject().enqueAndPocessReceiveData(go_request.get("data"))
                    session.up_seq = 1;
                    self.debug(True, "putSessionData", go_request.data + " post " + go_request.xmt_seq + " reset");
                else:
                    self.debug(True, "putSessionData", "(" + link_id + "," + session_id + ") "  + go_request.my_name + "=>" + go_request.his_name + " {" + go_request.data + "} " + go_request.xmt_seq + " dropped");
            else:
                self.logit("***abend: putSessionData", "%s post seq=%i dropped", go_request.get("data"), xmt_seq);

        self.debug(True, "putSessionData", "queue_size=%i", session.receiveQueue().size())
        return None

    def keepAlive(self, go_request):
        self.abend("keepAlive", "keepAlive is not implemented")
        return None


    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.farbricObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.farbricObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

