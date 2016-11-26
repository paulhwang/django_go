import go_server.phwang_modules.util_modules.logit

def malloc_mgr(host_object_val, global_id_val):
    return ListMgrClass(host_object_val, global_id_val)

def malloc_mgr_(host_object_val, global_id_val, name_val):
    list_mgr = ListMgrClass(host_object_val, global_id_val)
    list_mgr.setName(name_val)
    return list_mgr

def malloc_joint(entry_id_val):
    return ListjointClass(entry_id_val)

def head(list_mgr_val):
    if list_mgr_val == None:
        return None
    return list_mgr_val.head()

def next(host_object_val):
    if host_object_val == None:
        return None
    if host_object_val.jointObject().next() == None:
        return None
    return host_object_val.jointObject().next().hostObject()

class ListMgrClass(object):
    def __init__(self, host_object_val, global_id_val):
        self.theHostObject = host_object_val;
        self.theGlobalId = global_id_val
        self.theHead = None
        self.theTail = None
        self.theSize = 0
        self.debug(True, "init__", "")

    def objectName(self):
        return "ListMgrClass"

    def hostObject(self):
        return self.host_object_val

    def globalId(self):
        return self.theGlobalId

    def incrementGlobalId(self):
        self.theGlobalId += 1

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

    def globalId(self):
        return self.theGlobalId

    def incrementGlobalId(self):
        self.theGlobalId += 1

    def name(self):
        return self.theName

    def setName(self, val):
        self.theName = val

    def allocId(self):
        self.incrementGlobalId()
        return self.globalId()

    def insertEntry(self, link_val):
        if not link_val:
            self.abend("insertEntry", "null link_val")
            return

        self.abendIt()

        self.incrementSize()
        if not self.head():
            link_val.jointObject().setPrev(None)
            link_val.jointObject().setNext(None)
            self.setHead(link_val)
            self.setTail(link_val)
        else:
            self.tail().jointObject().setNext(link_val)
            link_val.jointObject().setPrev(self.tail())
            link_val.jointObject().setNext(None)
            self.setTail(link_val)
        self.abendIt()

    def deleteEntry(self, link_val):
        if self.size() <= 0:
            self.abend("deleteEntry", "size=%i", self.size())
            return
        if not self.linkExistInTheList(link_val):
            self.abend("deleteEntry", "linkExistInTheList is false")
            return

        self.abendIt()
        if link_val.jointObject().prev():
            link_val.jointObject().prev().jointObject().setNext(link_val.next())
        else:
            self.setHead(link_val.jointObject().next())
        if link_val.jointObject().next():
            link_val.jointObject().next().jointObject().setPrev(link_val.jointObject().prev())
        else:
            self.setTail(link_val.jointObject().prev())
        self.decrementSize()
        self.abendIt()

    def searchId(self, id_val):
        self.debug(False, "searchId",  "id=%i", id_val)
        entry = self.head()
        while entry:
            if (entry.jointObject().entryId() == id_val):
                return entry
            entry = entry.next()
        return None

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
            link = link.jointObject().next()
            i += 1
        if i != self.size():
            self.abend("abendIt", "head: size=%i i=%i", self.size(), i)

        i = 0
        link = self.tail()
        while link:
            link = link.jointObject().prev()
            i += 1
        if i != self.size():
            self.abend("abendIt", "tail: size=%i i=%i", self.size(), i)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def LOG_IT(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.logit.utilLogit(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def ABEND(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.phwang_modules.util_modules.logit.utilAbend(str1 + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

class ListjointClass(object):
    def __init__(self, entry_id_val):
        self.theEntryId = entry_id_val
        self.thePrev = None
        self.theNext = None

    def entryId(self):
        return self.theEntryId

    def prev(self):
        return self.thePrev

    def setPrev(self, val):
        self.thePrev = val

    def next(self):
        return self.theNext

    def setNext(self, val):
        self.theNext = val
