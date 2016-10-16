def malloc(util_val):
    return RingClass(util_val)

class RingClass(object):
    def __init__(self, util_val):
        self.theUtiObject = util_val

    def className(self):
        return "RingClass"

    def utiObject(self):
        return theUtiObject
