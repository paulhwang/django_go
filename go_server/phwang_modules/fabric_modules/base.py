def malloc(root_object_val):
    return BaseClass(root_object_val)

class BaseClass(object):
    def __init__(self, root_object_val):
        self.theRootObject = root_object_val
        self.theGlobalLinkId = 10
        self.debug(True, "init__", "")

    def objectName(self):
        return "BaseClass"

    def rootObject(self):
        return self.theRootObject

    def utilObject(self):
        return self.rootObject().utilObject()

    def linkMgrObject(self):
        return self.rootObject().linkMgrObject()

    def globalLinkId(self):
        return self.theGlobalLinkId

    def incrementGlobalLinkId(self):
        self.theGlobalLinkId += 1

    def mallocLink(self, my_name_val):
        link = self.rootObject().importObject().importLink().malloc(self.rootObject(), my_name_val, self.globalLinkId())
        self.incrementGlobalLinkId()
        self.linkMgrObject().insertLinkToList(link)
        self.setNameListChanged()
        return link

    def freeLink(self, link_val):
        self.linkMgrObject().deleteLinkFromList(link_val)

    def setNameListChanged(self):
        link = self.linkMgrObject().head()
        while link:
            link.setNameListChanged()
            link = link.next()

    def getNameList(self):
        name_array = []
        link = self.linkMgrObject().head()
        while link:
            name_array.append(link.myName())
            link = link.next()
        return name_array

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
