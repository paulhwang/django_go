import go_server.util_folder.queue

def malloc(fibre_val):
    return LinkMgrClass(fibre_val)

class LinkMgrClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val;
        self.theGlobalLinkId = 10;
        self.thePoolHead = 0;
        self.thePoolSize = 0;
        self.theLinkQueue = go_server.util_folder.queue.malloc();

    def className(self):
        return "LinkMgrClass"

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

