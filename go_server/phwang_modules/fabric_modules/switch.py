import json

def malloc(fabric_val):
    return SwitchClass(fabric_val)

class SwitchClass(object):
    def __init__(self, fabric_val):
        self.theFabricObject = fabric_val
        self.initSwitchTable()
        self.debug(True, "init__", "")

    def defaultLinkUpdateInterval(self):
        return 3000

    def debugInput(self):
        return False

    def debugOutput(self):
        return False

    def objectName(self):
        return "SwitchClass"

    def fabricObject(self):
        return self.theFabricObject

    def rootObject(self):
        return self.fabricObject().rootObject()

    def linkMgrObject(self):
        return self.fabricObject().linkMgrObject()

    def clusterMgrObject(self):
        return self.fabricObject().clusterMgrObject()

    def sessionMgrObject(self):
        return self.fabricObject().sessionMgrObject()

    def linkUpdateInterval(self):
        return self.theLinkUpdateInterval;

    def setLinkUpdateInterval(self, val):
        self.theLinkUpdateInterval = val;

    def initSwitchTable(self):
        self.switch_table = {
            "setup_link": self.setupLink,
            "get_link_data": self.getLinkData,
            "put_link_data": self.putLinkData,
            "get_name_list": self.getNameList,
            "setup_session": self.setupSession,
            "setup_session_reply": self.setupSessionReply,
            "get_session_data": self.getSessionData,
            "put_session_data": self.putSessionData,
            "keep_alive": self.keepAlive,
        }

    def switchRequest(self, input_val):
        go_request = json.loads(input_val)
        if go_request.get("command") == "get_link_data":
            self.debug_(False, self.debugInput(), "switchRequest", "input_val=%s", input_val)
        else:
            self.debug_(True, self.debugInput(), "switchRequest", "input_val=%s", input_val)

        if not go_request:
            self.abend("switchRequest", "null go_request")
            return None

        func = self.switch_table[go_request.get("command")]
        if func:
            return func(go_request)
        else:
            self.abend("switchRequest", "bad command=" + go_request.command)
            return None

    def setupLink(self, go_request):
        link = self.linkMgrObject().mallocLink(go_request.get("my_name"))
        if not link:
            self.abend("setupLink", "null link")
            return None
        link.resetKeepAliveTimer()
        self.setLinkUpdateInterval(self.defaultLinkUpdateInterval())

        json_data = json.dumps({"link_id": link.linkId()});
        output = json.dumps({"my_name": link.myName(),
                           "link_id": link.linkId(),
                          });
        self.debug_(True, self.debugOutput(), "setupLink", "output=%s", output)
        return output

    def getLinkObject(self, go_request):
        link = self.linkMgrObject().searchLinkByNameAndLinkId(go_request.get("my_name"), go_request.get("link_id"))
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

        if link.nameListChanged():
            self.debug(True, "getLinkData", "link.nameListChanged()=%s", link.nameListChanged());

        pending_session_setup = link.getPendingSessionSetup()
        if pending_session_setup:
            self.debug(True, "getLinkData", "pending_session_setup=%s", pending_session_setup);

        pending_session_data = link.getPendingSessionData()
        if pending_session_data:
            self.debug(True, "getLinkData", "pending_session_data=%s", pending_session_data);

        data = link.receiveQueue().deQueue()
        if data:
            self.debug(True, "getLinkData", "data=%s", data);

        output = json.dumps({"link_id": link.linkId(),
                           "name_list": link.nameListChanged(),
                           "data": data,
                           "pending_session_setup": pending_session_setup,
                           "pending_session_data": pending_session_data,
                           "interval": self.linkUpdateInterval(),
                           })
        self.debug_(False, self.debugOutput(), "getLinkData", "output=%s", output)
        return output

    def putLinkData(self, go_request):
        self.abend("putLinkData", "putLinkData is not implemented")
        return None

    def getNameList(self, go_request):
        link = self.getLinkObject(go_request)
        if not link:
            return None

        link.clearNameListChanged()
        output = json.dumps({"link_id": link.linkId(),
                                "name_list": self.linkMgrObject().getNameList(),
                                });
        self.debug_(True, self.debugOutput(), "getNameList", "output=%s", output)
        return output

    def setupSession(self, go_request):
        link = self.getLinkObject(go_request)
        if not link:
            return None

        session = link.mallocSession()
        if not session:
            return None

        cluster = self.clusterMgrObject().mallocCluster(go_request.get("topic_data"), session)
        if not cluster:
            return None


        if go_request.get("my_name") != go_request.get("his_name"):
            his_link = self.linkMgrObject().searchLinkByName(go_request.get("his_name"))
            if not his_link:
                return None
            his_session = his_link.mallocSession()
            if not his_session:
                return None
            cluster.addAdditionalSession(his_session)
            his_session.setClusterObject(cluster)
            his_link.setPendingSessionSetup(his_session, go_request.get("topic_data"))

        #if (go_request.topic_data !== null) {
            #session.clusterObject().processSetupTopicData(go_request.topic_data);

        output = json.dumps({
                        "link_id": link.linkId(),
                        "session_id": session.sessionId(),
                        "his_name": go_request.get("his_name"),
                        "topic_data": go_request.get("topic_data"),
                    });
        self.debug_(True, self.debugOutput(), "setupSession", "output=%s", output)
        return output

    def getSessionObject(self, go_request):
        link = self.linkMgrObject().searchLinkByLinkId(go_request.get("link_id"))
        if not link:
            self.logit("getSessionObject", "link not found: link_id=%i", go_request.gt("link_id"))
            return None

        session = link.searchSessionBySessionId(go_request.get("session_id"))
        if not session:
            self.abend("getSessionObject", "null session session_id=%s", go_request.get("session_id"))
            return None

        return session

    def setupSessionReply(self, go_request):
        session = self.getSessionObject(go_request)
        if not session:
            return None
        output = json.dumps({"link_id": session.linkObject().linkId(),
                           "session_id": session.sessionId(),
                           "confirm": "yes",
                           "topic_data": go_request.get("topic_data"),
                           "his_name": "tbd",
                           })
        self.debug_(True, self.debugOutput(), "setupSessionReply", "output=%s", output)
        return output

    def getSessionData(self, go_request):
        session = self.getSessionObject(go_request)
        if not session:
            return None

        res_data = session.dequeueTransmitData()
        if not res_data:
            self.debug(True, "getSessionData", "no data")
            return None

        self.debug(False, "getSessionData", "ajax_id=%i", go_request.get("ajax_id"))
        self.debug(True, "getSessionData", "(%i,%i %s=>%s) {%s}", go_request.get("link_id"), go_request.get("session_id"), go_request.get("his_name"), go_request.get("my_name"), res_data)

        output = json.dumps({"link_id": session.linkObject().linkId(),
                           "session_id": session.sessionId(),
                           "res_data": res_data,
                           })
        self.debug_(True, self.debugOutput(), "getSessionData", "output=%s", output)
        return output

    def putSessionData(self, go_request):
        session = self.getSessionObject(go_request)
        if not session:
            return None

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

        res_data = session.dequeueTransmitData()
        if not res_data:
            self.debug(True, "putSessionData", "no data")
            return None

        output = json.dumps({"link_id": session.linkObject().linkId(),
                           "session_id": session.sessionId(),
                           "res_data": res_data,
                           })
        self.debug_(True, self.debugOutput(), "putSessionData", "output=%s", output)
        return output

    def keepAlive(self, go_request):
        self.abend("keepAlive", "keepAlive is not implemented")
        return None


    def debug_(self, debug_val, debug_val_, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if debug_val and debug_val_:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def debug(self, debug_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if debug_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
