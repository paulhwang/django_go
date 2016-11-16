def malloc(util_val):
    return QueueClass(util_val)

class QueueClass(object):
    def __init__(self, util_val):
        self.theUtilObject = util_val
        self.theSize = 0
        self.theHead = None
        self.theTail = None
        self.theHolderPoolObject = HolderPoolClass(self)
        self.theRing = self.utilObject().mallocRing()

    def debugRing(self):
        return True

    def className(self):
        return "QueueClass"

    def utilObject(self):
        return self.theUtilObject

    def phwangObject(self):
        return self.utilObject().phwangObject()

    def ring(self):
        return self.theRing

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
        if not data_val:
            self.abend("enQueue", "null data_val")
            return

        if self.debugRing():
            i = 10
            while (i > 0):
                self.ring().enQueue(data_val)
                i -= 1;

        self.abendIt()

        data_entry = self.holderPoolObject().mallocEntry(data_val)
        if not data_entry:
            self.abend("enQueue", "null data_entry")
            return

        self.incrementSize()

        if not self.head():
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
        data_entry = None
        data = None

        self.debug(0, "deQueue", "start")
        self.abendIt()

        if not self.head():
            data_entry = None
            data = None
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
            self.holderPoolObject().freeEntry(data_entry)

        self.abendIt()

        if self.debugRing():
            i = 10
            while (i > 0):
                data1 = self.ring().deQueue()
                if data != data1:
                    self.abend("deQueue", "ring not match")
                i -= 1

        return data

    def unQueue(self, func_val, input_val1, input_val2, input_val3):
        self.abendIt()

        p = self.head()
        while p:
            self.debug(false, "unQueue", "in while loop")
            p = p.next()

        self.abendIt()
        self.debug(false, "unQueue", "not found")

    def searchIt(self, func_val, input_val1, input_val2, input_val3):
        p = self.head();
        while p:
            self.debug(False, "searchIt", "in while loop")
            if func_val(p.data(), input_val1, input_val2, input_val3):
                self.debug(False, "searchIt", "found")
                return p.data()
            p = p.next()
        self.debug(False, "searchIt", "not found")
        return None

    def abendIt(self):
        i = 0
        p = self.head()
        while p:
            p = p.next()
            i += 1

        if i != self.size():
            i = self.abend("abendIt", "head: size=%i i=", self.size(), i)

        i = 0
        p = self.tail()
        while p:
            p = p.prev()
            i += 1

        if i != self.size():
            i = self.abend("abendIt", "tail: size=%i i=", self.size(), i)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.phwangObject().logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.phwangObject().abend(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)


class HolderPoolClass(object):
    def __init__(self, queue_val):
        self.theQueueObject = queue_val
        self.theHead = None
        self.theTail = None
        self.theSize = 0

    def queueObject(self):
        return self.theQueueObject

    def utilObject(self):
        return self.queueObject().utilObject()

    def phwangObject(self):
        return self.utilObject().phwangObject()

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

        if not self.head():
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
        if not entry_val:
            return

        self.abendIt()
        self.incrementSize()
        entry_val.setNext(self.head())
        self.setHead(entry_val)

        self.abendIt()

    def abendIt(self):
        i = 0
        p = self.head()
        while p:
            p = p.next()
            i += 1

        if i != self.size():
            self.abend("abendIt", "size=" + self.size() + " i=" + i)

        if self.size() > 5:
            self.abend("abendIt", " size=" + self.size())

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.phwangObject().logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.phwangObject().abend(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)


class HolderEntryClass(object):
    def __init__(self):
        self.theData = None
        self.thePrev = None
        self.theNext = None

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
