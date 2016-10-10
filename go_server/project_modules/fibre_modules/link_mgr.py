import go_server.project_modules.util_modules.queue

def malloc(fibre_val):
    return LinkMgrClass(fibre_val)

class LinkMgrClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val;
        self.theGlobalLinkId = 10;
        self.thePoolHead = 0;
        self.thePoolSize = 0;
        self.theLinkQueue = go_server.project_modules.util_modules.queue.malloc();

    def className(self):
        return "LinkMgrClass"

    def fibreObject(self):
        return self.theFibreObject

    def poolHead(self):
        return self.thePoolHead

    def setPoolHead(self, val):
        self.thePoolHead = val

    def poolSize(self):
        return self.thePoolSize

    def incrementPoolSize(self):
        self.thePoolSize += 1

    def decrementPoolSize(self):
        self.thePoolSize -= 1

    def mallocIt(self, my_name_val):
        entry = 0;
        if self.poolHead() == 0:
            entry = self.linkModule().malloc(my_name_val, self.globalLinkId())
        else:
            entry = self.poolHead()
            entry.resetIt(my_name_val, self.globalLinkId())
            self.setHead(entry.next())
            self.decrementPoolSize()

        self.incrementGlobalLinkId()

        self.abendIt()
        return entry

    def freeIt(self, entry_val):
        self.incrementPoolSize()
        entry_val.setNext(self.poolHead())
        self.setHead(entry_val)
        self.abendIt()

    def abendIt(self):
        i = 0
        p = self.poolHead()
        while p != 0:
            p = p.next()
            i += 1

        if i != self.poolSize():
            self.abend("abendIt", "size=" + self.poolSize() + " i=" + i)

        if self.poolSize() > 5:
            self.abend("abendIt", "size=" + self.poolSize())

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

