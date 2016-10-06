def malloc():
    return QueueClass()

class QueueClass(object):
    def __init__(self):
        self.theSize = 0;
        self.theHead = 0;
        self.theTail = 0;
        self.theHolderPoolObject = HolderPoolClass()

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

    def abend(self, str1, str2):
        return 0

    def enQueue(self, data_val):
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

    def deQueue(self):
        self.decrementSize()

    def abendIt(self):
        i = 0
        p = self.head()
        while p != 0:
            p = p.next()
            i += 1

        if i != self.size():
            i = 999 #self.abend("abendIt", "head: size=%i i=", self.size(), i)

        i = 0
        p = self.tail()
        while p != 0:
            p = p.prev()
            i += 1

        if i != self.size():
            i = 999 #self.abend("abendIt", "tail: size=%i i=", self.size(), i)

class HolderPoolClass(object):
    def __init__(self):
        self.theHead = 0
        self.theTail = 0
        self.heSize = 0

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

    def abendIt(self):
        return 1

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
