def malloc(root_Object_val):
    return RingClass(root_Object_val)

class RingClass(object):
    def __init__(self, root_Object_val):
        self.theRootObject = root_Object_val
        self.theInput = 0
        self.theOutput = 0
        self.theSize = 2
        self.theLeft = self.size()
        self.theArray = [None] * self.size()
        self.debug(True, "init__", "")

    def objectName(self):
        return "RingClass"

    def rootObject(self):
        return self.theRootObject

    def input(self):
        return self.theInput

    def setInput(self, val):
        self.theInput = val

    def incrementInput(self):
        self.theInput += 1

    def output(self):
        return self.theOutput

    def setOutput(self, val):
        self.theOutput = val

    def incrementOutput(self):
        self.theOutput += 1

    def size(self):
        return self.theSize

    def setSize(self, val):
        self.theSize = val

    def incrementSize(self):
        self.theSize += 1

    def decrementSize(self):
        self.theSize -= 1

    def left(self):
        return self.theLeft

    def setLeft(self, val):
        self.theLeft = val

    def incrementLeft(self):
        self.theLeft += 1

    def decrementLeft(self):
        self.theLeft -= 1

    def array(self, index_val):
        return self.theArray[index_val]

    def setArray(self, index_val, data_val):
        self.theArray[index_val] = data_val

    def enQueue(self, data_val):
        if self.left() < 0:
            self.abend("enQueue", "left=%i", self.left())
            return

        if self.left() <= (self.size() / 2):
            self.enlargeSize()

        self.setArray(self.input(), data_val)
        self.incrementInput()
        if self.input() == self.size():
            self.setInput(0)
        self.decrementLeft()
        self.abendIt()

    def deQueue(self):
        if self.left() == self.size():
            return None

        data = self.array(self.output())
        self.incrementOutput()
        if self.output() == self.size():
            self.setOutput(0)

        self.incrementLeft()
        self.abendIt()
        return data

    def enlargeSize(self):
        self.debug(False, "enlargeSize", "size=%i=>%i", self.size(), self.size() * 2)

        old_array = self.theArray;
        self.theArray = [None] * (self.size() * 2)

        i = 0
        while i < self.size():
            self.setArray(i, old_array[i])
            i += 1

        if self.input() < self.output():
            i = 0
            while i <= self.input():
                self.setArray(self.size() + i, i)
                i += 1
            self.input += self.size()

        self.setLeft(self.left() + self.size())
        self.setSize(self.size() * 2)

        self.abendIt()

    def abendIt(self):
        if self.left() < 0:
            self.abend("abendIt", "left=%i", self.left())

        if (self.input() + self.left() - self.output() != self.size()) and (self.input() + self.left() - self.output() != 0):
            self.abend('abendIt', "input(" + self.input() + ") + left(" + self.left() + ") - output(" + self.output() + ") !== size(" + self.size() + ")");

    def debug(self, debug_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if debug_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
