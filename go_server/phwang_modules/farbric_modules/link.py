def malloc(link_mgr_val, my_name_val, link_id_val):
    return LinkClass(link_mgr_val, my_name_val, link_id_val)

class LinkClass(object):
    def __init__(self, link_mgr_val, my_name_val, link_id_val):
        self.theLinkMgrObject = link_mgr_val;
        self.theKeepAliveTimer = None
        self.resetIt(my_name_val, link_id_val)

    def className(self):
        return "LinkClass"

    def linkMgrObject(self):
        return self.theLinkMgrObject

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

    def keepAliveTimer(self):
        return self.theKeepAliveTimer

    def setKeepAliveTimer(self, val):
        self.theKeepAliveTimer = val

    def receiveQueue(self):
        return self.theReceiveQueue;

    def receiveRing(self):
        return self.theReceiveRing;

    def nameListChanged(self):
        return self.theNameListChanged

    def setNameListChanged(self):
        self.theNameListChanged = True

    def clearNameListChanged(self):
        self.theNameListChanged = False

    def resetIt(self, my_name_val, link_id_val):
        self.theMyName = my_name_val
        self.theLinkId = link_id_val
        self.up_seq = 0
        self.down_seq = 0
        self.theReceiveQueue = self.utilObject().mallocQueue()
        self.theReceiveRing = self.utilObject().mallocRing()
        self.theKeepAliveTimer = self.resetTimeout()
        self.theNameListChanged = True

    def resetKeepAliveTimer(self):
        self.debug(False, "resetKeepAliveTimer", "my_name=%s link_id=%i", self.myName(), self.linkId())
        self.setKeepAliveTimer(self.resetTimeout())

    def resetTimeout(self):
        if self.keepAliveTimer():
            clearInterval(self.keepAliveTimer())

        self.debug(False, "resetTimeout", "my_name=%s link_id=%i", self.myName(), self.linkId())
        #time_out = setInterval(function (link_val) {
        #    console.log("resetTimeout(***timeout occurs)", "my_name=" + link_val.myName() + " link_id=" + link_val.linkId());
        #    clearInterval(link_val.keepAliveTimer());
        #    link_val.linkMgrObject().freeLink(link_val);
        #}, 20000, self);
        #return time_out;
        return None

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.linkMgrObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.linkMgrObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
