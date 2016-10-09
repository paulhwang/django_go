import go_server.project_modules.util_modules.queue

def malloc(fibre_val):
    return SessionMgrClass(fibre_val)

class SessionMgrClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val
        self.theSessionQueue = go_server.project_modules.util_modules.queue.malloc()
        self.thePreSessionQueue = go_server.project_modules.util_modules.queue.malloc()
        self.theGlobalSessionId = 1000
        self.thePoolHead = 0
        self.thePoolSize = 0

    def className(self):
        return "SessionMgrClass"

    def fibreObject(self):
        return self.theFibreObject

    def sessionQueue(self):
        return self.theSessionQueue;

    def preSessionQueue(self):
        return self.thePreSessionQueue;

    def globalSessionId(self):
        return self.theGlobalSessionId;

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


