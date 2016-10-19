import go_server.project_modules.farbric_modules.link

def malloc(fabric_val):
    return LinkMgrClass(fabric_val)

def malloc_link(link_mgr_val, my_name_val, link_id_val):
    return go_server.project_modules.farbric_modules.link.malloc(link_mgr_val, my_name_val, link_id_val)

class LinkMgrClass(object):
    def __init__(self, fabric_val):
        self.theFarbricObject = fabric_val
        self.theGlobalLinkId = 10
        self.theLinkQueue = self.utilObject().mallocQueue()
        self.thePoolQueue = self.utilObject().mallocQueue()

    def linkModuleMalloc(self, my_name_val, link_id_val):
        return malloc_link(self, my_name_val, link_id_val)

    def className(self):
        return "LinkMgrClass"

    def farbricObject(self):
        return self.theFarbricObject

    def phwangObject(self):
        return self.farbricObject().phwangObject()

    def utilObject(self):
        return self.phwangObject().utilObject()

    def linkQueue(self):
        return self.theLinkQueue

    def poolQueue(self):
        return self.thePoolQueue

    def globalLinkId(self):
        return self.theGlobalLinkId

    def incrementGlobalLinkId(self):
        self.theGlobalLinkId += 1

    def searchLink(self, my_name_val, link_id_val):
        self.debug(False, "searchLink", "my_name=%s link_id=%s", my_name_val, link_id_val)
        return self.linkQueue().searchIt(compareFunction, my_name_val, link_id_val, None)
        #return self.linkQueue().searchIt(function (link_val, my_name_val, link_id_val) {
        #    return ((my_name_val === link_val.myName()) &&
         #           ((link_id_val === link_val.linkId()) || (link_id_val === 0)));
        #}, my_name_val, link_id_val);

    def searchAndCreate(self, my_name_val, link_id_val):
        link = self.searchLink(my_name_val, link_id_val)
        if not link:
            link = self.mallocLink(my_name_val)
            self.debug(True, "searchAndCreate", "malloc link: name=%s link_id=%i", link.myName(), link.linkId())
            self.linkQueue().enQueue(link)
        return link

    def getNameList(self):
        name_array = [None] * self.linkQueue().size()
        i = 0
        queue_element = self.linkQueue().tail()
        while queue_element:
            link = queue_element.data()
            name_array[i] = link.myName()
            i += 1
            queue_element = queue_element.prev()
        return name_array

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
        self.farbricObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.farbricObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

def compareFunction(link_val, my_name_val, link_id_val, dummy_val):
    if my_name_val != link_val.myName():
        return False
    if (link_id_val == link_val.linkId() or link_id_val == 0):
        return True
    return False
