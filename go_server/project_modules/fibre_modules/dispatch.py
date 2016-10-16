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

        link_id_str = "" + link.linkId()
        self.debug(True, "setupLink", "name=%s link_id=%i", go_request.get("my_name"), link.linkId())
        return link_id_str

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

