def malloc(go_val):
    return GoGameClass(go_val)

class GoGameClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val;

    def className(self):
        return "GoGameClass"

    def goObject(self):
        return theGoObject