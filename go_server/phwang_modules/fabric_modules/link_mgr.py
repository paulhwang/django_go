import go_server.phwang_modules.fabric_modules.link

def malloc(fabric_val):
    return LinkMgrClass(fabric_val)

def malloc_link(link_mgr_val, my_name_val, link_id_val):
    return go_server.phwang_modules.fabric_modules.link.malloc(link_mgr_val, my_name_val, link_id_val)

class LinkMgrClass(object):
    def __init__(self, fabric_val):
        self.theFabricObject = fabric_val
        self.theGlobalLinkId = 10
        self.theHead = None
        self.theTail = None
        self.theSize = 0

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

    def globalLinkId(self):
        return self.theGlobalLinkId

    def incrementGlobalLinkId(self):
        self.theGlobalLinkId += 1

    def head(self):
        return self.theHead

    def setHead(self, val):
        self.theHead = val

    def tail(self):
        return self.theTail

    def setTail(self, val):
        self.theTail = val

    def size(self):
        return self.theSize

    def incrementSize(self):
        self.theSize += 1

    def decrementSize(self):
        self.theSize -= 1

    def mallocLink(self, my_name_val):
        link = self.linkModuleMalloc(my_name_val, self.globalLinkId())
        self.incrementGlobalLinkId()
        self.insertLinkToList(link)
        self.setNameListChanged()
        return link

    def freeLink(self, link_val):
        self.deleteLinkFromList(link_val)

    def insertLinkToList(self, link_val):
        if not link_val:
            self.abend("enQueue", "null link_val")
            return

        self.abendIt()

        self.incrementSize()
        if not self.head():
            link_val.setPrev(None)
            link_val.setNext(None)
            self.setHead(link_val)
            self.setTail(link_val)
        else:
            self.tail().setNext(link_val)
            link_val.setPrev(self.tail())
            link_val.setNext(None)
            self.setTail(link_val)
        self.abendIt()

    def deleteLinkFromList(self, link_val):
        if self.size() <= 0:
            self.abend("deleteLinkFromList", "size=%i", self.size())
            return
        if not self.linkExistInTheList(link_val):
            self.abend("deleteLinkFromList", "linkExistInTheList is false")
            return

        self.abendIt()
        if link_val.prev():
            link_val.prev().setNext(link_val.next())
        else:
            self.setHead(link_val.next())
        if link_val.next():
            link_val.next().setPrev(link_val.prev())
        else:
            self.setTail(link_val.prev())
        self.decrementSize()
        self.abendIt()

    def searchLinkByNameAndLinkId(self, my_name_val, link_id_val):
        self.debug(False, "searchLinkByNameAndLinkId name=%s id=%i", my_name_val, link_id_val)
        link = self.head()
        while link:
            if (link.linkId() == link_id_val) and (link.myName() == my_name_val):
                return link
            link = link.next()
        return None

    def searchLinkByName(self, my_name_val):
        self.debug(False, "searchLinkByName name=%s", my_name_val)
        link = self.head()
        while link:
            if link.myName() == my_name_val:
                return link
            link = link.next()
        return None

    def linkExistInTheList(self, link_val):
        link = self.head()
        while link:
            if link == link_val:
                return True
            link = link.next()
        return False

    def setNameListChanged(self):
        link = self.head()
        while link:
            link.setNameListChanged()
            link = link.next()

    def getNameList(self):
        name_array = []
        link = self.head()
        while link:
            name_array.append(link.myName())
            link = link.next()
        return name_array

    def abendIt(self):
        i = 0;
        link = self.head()
        while link:
            link = link.next()
            i += 1
        if i != self.size():
            self.abend("abendIt", "head: size=%i i=%i", self.size(), i)

        i = 0
        link = self.tail()
        while link:
            link = link.prev()
            i += 1
        if i != self.size():
            self.abend("abendIt", "tail: size=%i i=%i", self.size(), i)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fabricObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fabricObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
