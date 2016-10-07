def malloc(go_val):
    return GoMoveClass(go_val)

class GoMoveClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val;

    def className(self):
        return "GoMoveClass"

    def goObject(self):
        return theGoObject