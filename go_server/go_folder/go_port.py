def malloc(go_val):
    return GoPortClass(go_val)

class GoPortClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val;

    def className(self):
        return "GoPortClass"

    def goObject(self):
        return self.theGoObject

    def gameObject(self):
        return self.goObject().gameObject()

    def forNow(self, str_val):
        move = self.goObject().mallocMove(str_val, 0, 0, 0, 0, self.goObject())
        self.gameObject().addNewMoveAndFight(move)
