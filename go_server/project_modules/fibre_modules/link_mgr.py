def malloc(fibre_val):
    return LinkMgrClass(fibre_val)

class LinkMgrClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val
        self.theGlobalLinkId = 10
        self.theLinkQueue = self.utilObject().mallocQueue()
        self.thePoolQueue = self.utilObject().mallocQueue()

    def className(self):
        return "LinkMgrClass"

    def fibreObject(self):
        return self.theFibreObject

    def rootObject(self):
        return self.fibreObject().rootObject()

    def utilObject(self):
        return self.rootObject().utilObject()

    def poolQueue(self):
        return self.thePoolQueue

    def searchLink(self, my_name_val, link_id_val):
        self.debug(True, "searchIt", "my_name=%s link_id=%s", my_name_val, link_id_val)
        #return self.linkQueue().searchIt(function (link_val, my_name_val, link_id_val) {
        #    return ((my_name_val === link_val.myName()) &&
        #            ((link_id_val === link_val.linkId()) || (link_id_val === 0)));
        #}, my_name_val, link_id_val);

    def searchAndCreate(self, my_name_val, link_id_val):
        link = self.searchLink(my_name_val, link_id_val)
        if not link:
            link = self.mallocLink(my_name_val)
            self.debug(False, "searchAndCreate", "malloc link: name=" + link.myName() + "=link_id=" + link.link_id)
            self.linkQueue().enQueue(link)
        return link

    def mallocLink(self, my_name_val):
        entry = self.poolQueue().deQueue()
        if not entry:
            entry = self.linkModuleMalloc(my_name_val, self.globalLinkId())
        else:
            entry.resetIt(my_name_val, self.globalLinkId())
        self.incrementGlobalLinkId()
        return entry

    def freeLink(self, link_val):
        self.poolQueue().enQueue(link_val)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

