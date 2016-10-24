import go_server.phwang_modules.farbric_modules.link

def malloc(fabric_val):
    return LinkMgrClass(fabric_val)

def malloc_link(link_mgr_val, my_name_val, link_id_val):
    return go_server.phwang_modules.farbric_modules.link.malloc(link_mgr_val, my_name_val, link_id_val)

class LinkMgrClass(object):
    def __init__(self, fabric_val):
        self.theFabricObject = fabric_val
        self.theGlobalLinkId = 10
        self.theLinkQueue = self.utilObject().mallocQueue()
        self.thePoolQueue = self.utilObject().mallocQueue()

    def linkModuleMalloc(self, my_name_val, link_id_val):
        return malloc_link(self, my_name_val, link_id_val)

    def className(self):
        return "LinkMgrClass"

    def fabricObject(self):
        return self.theFabricObject

    def phwangObject(self):
        return self.fabricObject().phwangObject()

    def utilObject(self):
        return self.phwangObject().utilObject()

    def linkQueue(self):
        return self.theLinkQueue

    def globalLinkId(self):
        return self.theGlobalLinkId

    def incrementGlobalLinkId(self):
        self.theGlobalLinkId += 1

    def searchLinkByName(self, my_name_val):
        self.debug(False, "searchLinkByName", "name=%s", my_name_val);
        return self.linkQueue().searchIt(compareNameFunction_, my_name_val, None, None)

    def searchLinkByLinkId(self, link_id_val):
        self.debug(False, "searchLinkByLinkId", "link_id=%i", link_id_val);
        return self.linkQueue().searchIt(compareLinkIdFunction_, link_id_val, None, None)

    def searchLinkByNameAndLinkId(self, my_name_val, link_id_val):
        self.debug(False, "searchLinkByNameAndLinkId", "my_name=%s link_id=%s", my_name_val, link_id_val)
        return self.linkQueue().searchIt(compareNameAndLinkIdFunction_, my_name_val, link_id_val, None)

    def searchAndCreate(self, my_name_val):
        link = self.searchLinkByName(my_name_val)
        if not link:
            link = self.mallocLink(my_name_val)
            self.debug(True, "searchAndCreate", "malloc link: name=%s link_id=%i", link.myName(), link.linkId())
            self.setNameListChanged();
            self.linkQueue().enQueue(link)
        return link

    def setNameListChanged(self):
        queue_element = self.linkQueue().tail()
        while queue_element:
            link = queue_element.data()
            link.setNameListChanged()
            queue_element = queue_element.prev()

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
        entry = self.linkModuleMalloc(my_name_val, self.globalLinkId())
        self.incrementGlobalLinkId()
        return entry

    #def freeLink(self, link_val):

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fabricObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fabricObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

def compareNameAndLinkIdFunction_(link_val, my_name_val, link_id_val, dummy_val):
    return  (my_name_val == link_val.myName()) and (link_id_val == link_val.linkId() or link_id_val == 0)

def compareNameFunction_(link_val, my_name_val, dummy_val3, dummy_val4):
    return my_name_val == link_val.myName()

def compareLinkIdFunction_(link_val, link_id_val, dummy_val3, dummy_val4):
    return link_id_val == link_val.linkId()
