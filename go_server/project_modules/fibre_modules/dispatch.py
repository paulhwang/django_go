import json

def malloc(fibre_val):
    return DispatchClass(fibre_val)

class DispatchClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val;

    def className(self):
        return "DispatchClass"

    def fibreObject(self):
        return self.theFibreObject

    def linkMgrObject(self):
        return self.fibreObject().linkMgrObject()

    def sessionMgrObject(self):
        return self.fibreObject().sessionMgrObject()

    def dispatchRequest(self, go_request):
        self.debug(False, "dispatchRequest", "command=%s", go_request["command"])

        if go_request["command"] == "setup_link":
            return self.setupLink(go_request)

        if go_request["command"] == "keep_alive":
            self.abend("dispatchRequest", "keep_alive gorequest=")
            return self.keepAlive(go_request)

        if go_request["command"] == "get_link_data":
            return self.getLinkData(go_request)

        if go_request["command"] == "put_link_data":
            self.abend("dispatchRequest", "put_link_data")
            return self.putLinkData(go_request)

        if go_request["command"] == "get_name_list":
            return self.getNameList(go_request)

        if go_request["command"] == "setup_session":
            return self.setupSession(go_request)

        if go_request["command"] == "get_session_data":
            return self.getSessionData(go_request)

        if go_request["command"] == "put_session_data":
            return self.putSessionData(go_request)

        self.abend("dispatchRequest", "command=%s", go_request["command"])


    def setupLink(self, go_request):
        if not go_request:
            self.abend("setupLink", "null go_request")
            return None

        link = self.linkMgrObject().searchAndCreate(go_request.get("my_name"), 0)
        if not link:
            self.abend("setupLink", "null link")
            return None
        link.resetKeepAliveTimer()

        link_id_str = str(link.linkId())
        self.debug(False, "setupLink", "name=%s link_id=%i", go_request.get("my_name"), link.linkId())
        return link_id_str

    def getLink(self, go_request):
        link = self.linkMgrObject().searchLink(go_request.get("my_name"), go_request.get("link_id"))
        if not link:
            self.abend("getLink", "null link: link_id=%i my_name=%s", go_request.get("link_id"), go_request.get("my_name"))
            return None
        if link.linkId() == 0:
            self.abend("getLink", "link_id = 0")
            return None
        return link

    def getLinkData(self, go_request):
        self.debug(False, "getLinkData", "link_id=%i my_name=%s ajax_id=%i", go_request.get("link_id"), go_request.get("my_name"), go_request.get("ajax_id"))

        link = self.getLink(go_request)
        if not link:
            return None
        link.resetKeepAliveTimer()

        data = link.receiveQueue().deQueue()
        if data:
            self.debug(False, "getLinkData", "link_id=%i my_name=%s data={%s}", go_request.link_id, go_request.my_name, data);
        return data

    def getNameList(self, go_request):
        link = self.getLink(go_request)
        if not link:
            return None
        link.resetKeepAliveTimer()

        name_array = self.linkMgrObject().getNameList()
        name_array_str = json.dumps(name_array)
        self.debug(True, "getNameList", "link_id=%i my_name=%s data=%s", link.linkId(), go_request.get("my_name"), name_array_str);
        return name_array_str

    def setupSession (self, go_request):
        session = self.sessionMgrObject().searchSession(go_request.get("my_name"), go_request.get("his_name"), go_request.get("link_id"))
        if not session:
            session = self.sessionMgrObject().searchAndCreate(go_request.get("my_name"), go_request.get("his_name"), 0)
            if not session:
                res.send(self.jsonStingifyData(go_request.command, go_request.ajax_id, null))
                self.abend("setupSession", "null session")
                return None

        his_link = self.linkMgrObject().searchLink(go_request.his_name, 0)
        if not his_link:
            res.send(self.jsonStingifyData(go_request.command, go_request.ajax_id, null))
            return None

        self.debug(True, "setupSession", "(" + go_request.link_id + "," + session.sessionId() + "," + session.hisSession().sessionId() + ") " + go_request.my_name + "=>" + go_request.his_name + " data=" + go_request.data)

        if go_request.data != None:
            session.clusterObject().processSetupLinkData(go_request.data)

        session_id_str = "" + session.hisSession().sessionId()
        data = JSON.stringify({
                        order: "setup_session",
                        session_id: session_id_str,
                        his_name: go_request.my_name,
                        my_name: go_request.his_name,
                        extra_data: go_request.data,
                    });
        his_link.receiveQueue().enQueue(data);
        self.sessionMgrObject().preSessionQueue().enQueue(data)
        return self.setupSessionReply(session, go_request);

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

