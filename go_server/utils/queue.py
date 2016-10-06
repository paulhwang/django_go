def malloc():
    return QueueClass()

class QueueClass(object):
    size = 0

    def queueSize(self):
    	return self.size

    def enqueueIt(self):
        self.size += 1

    def dequeueIt(self):
    	self.size -= 1
