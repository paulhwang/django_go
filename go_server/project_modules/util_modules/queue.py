import go_server.project_modules.util_modules.util

def malloc(util_val):
    return QueueClass(util_val)

class QueueClass(object):
    def __init__(self, util_val):
        self.theUtiObject = util_val
        self.theSize = 0;
        self.theHead = 0;
        self.theTail = 0;
        self.theHolderPoolObject = HolderPoolClass()

    def className(self):
        return "QueueClass"

    def utiObject(self):
        return theUtiObject

    def size(self):
        return self.theSize

    def incrementSize(self):
        self.theSize += 1

    def decrementSize(self):
        self.theSize -= 1

    def head(self):
        return self.theHead

    def setHead(self, val):
        self.theHead = val

    def tail(self):
        return self.theTail

    def setTail(self, val):
        self.theTail = val

    def holderPoolObject(self):
        return self.theHolderPoolObject

    def enQueue(self, data_val):
        self.debug(0, "enQueue", "start")
        #self.debug(1, "enQueue", "start %i", 100)
        #self.debug(1, "enQueue", "start %i %s", 100, "A")
        #self.debug(1, "enQueue", "start %i %s %i", 100, "b", 1000)
        #self.debug(1, "enQueue", "start %i %s %i %i", 100, "b", 1000, 1)
        #self.debug(1, "enQueue", "start %i %s %i %i %i", 100, "b", 1000, 1, 1)
        if data_val == 0:
            self.abend("enQueue", "null data_val")
            return

        self.abendIt()

        data_entry = self.holderPoolObject().mallocEntry(data_val)
        if data_entry == 0:
            self.abend("enQueue", "null data_entry")
            return

        self.incrementSize()

        if self.head() == 0:
            data_entry.setPrev(0)
            data_entry.setNext(0)
            self.setHead(data_entry)
            self.setTail(data_entry)
        else:
            self.tail().setNext(data_entry)
            data_entry.setPrev(self.tail())
            data_entry.setNext(0)
            self.setTail(data_entry)

        self.abendIt()
        self.debug(0, "enQueue", "end")

    def deQueue(self):
        data_entry = 0
        data = 0

        self.debug(0, "deQueue", "start")
        self.abendIt()

        if self.head() == 0:
            data_entry = 0
            data = 0
        else:
            if self.head() == self.tail():
                self.decrementSize()
                data_entry = self.head()
                data = data_entry.data()
                self.setHead(0)
                self.setTail(0)
            else:
                self.decrementSize()
                data_entry = self.head()
                data = data_entry.data()
                self.setHead(self.head().next())
                self.head().setPrev(0)

        if data_entry:
            #elf.logit("deQueue", "data=" + data_entry.data)
            self.holderPoolObject().freeEntry(data_entry)
        else:
            self.logit("deQueue", "null")

        self.abendIt()
        self.debug(0, "deQueue", "end")
        return data

    def unQueue(self, func_val, input_val1, input_val2, input_val3):
        self.abendIt()

        p = self.head()
        while p != 0:
            self.debug(false, "unQueue", "in while loop")
            p = p.next()

        self.abendIt()
        self.debug(false, "unQueue", "not found")

    def abendIt(self):
        i = 0
        p = self.head()
        while p != 0:
            p = p.next()
            i += 1

        if i != self.size():
            i = self.abend("abendIt", "head: size=%i i=", self.size(), i)

        i = 0
        p = self.tail()
        while p != 0:
            p = p.prev()
            i += 1

        if i != self.size():
            i = self.abend("abendIt", "tail: size=%i i=", self.size(), i)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val != 0:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.utils.util.utilLogit(self.className() + "." + str1 + "() " + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.utils.util.utilAbend(self.className() + "." + str1 + "() " + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

class HolderPoolClass(object):
    def __init__(self):
        self.theHead = 0
        self.theTail = 0
        self.theSize = 0

    def head(self):
        return self.theHead

    def setHead(self, val):
        self.theHead = val

    def size(self):
        return self.theSize;

    def incrementSize(self):
        self.theSize += 1

    def decrementSize(self):
        self.theSize -= 1

    def mallocEntry(self, data_val):
        entry = 0

        self.abendIt()

        if self.head() == 0:
            entry = HolderEntryClass()
        else:
            entry = self.head()
            self.setHead(entry.next())
            self.decrementSize()

        self.abendIt()

        if entry:
            entry.setData(data_val)
        else:
            self.abend('mallocEntry', 'null')

        return entry

    def freeEntry(self, entry_val):
        self.abendIt()
        if entry_val == 0:
            return

        self.abendIt()
        self.incrementSize()
        entry_val.setNext(self.head())
        self.setHead(entry_val)

        self.abendIt()

    def abendIt(self):
        i = 0
        p = self.head()
        while p != 0:
            p = p.next()
            i += 1

        if i != self.size():
            self.abend("abendIt", "size=" + self.size() + " i=" + i)

        if self.size() > 5:
            self.abend("abendIt", " size=" + self.size())

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val != 0:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.utils.util.utilLogit(self.className() + "." + str1 + "() " + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        go_server.utils.util.utilAbend(self.className() + "." + str1 + "() " + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

class HolderEntryClass(object):
    def __init__(self):
        self.theData = 0;
        self.thePrev = 0;
        self.theNext = 0;

    def data(self):
        return self.theData

    def setData(self, val):
        self.theData = val

    def prev(self):
        return self.thePrev

    def setPrev(self, val):
        self.thePrev = val

    def next(self):
        return self.theNext

    def setNext (self, val):
        self.theNext = val;
