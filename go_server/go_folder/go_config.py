def malloc(go_val):
    return ConfigClass(go_val)

class ConfigClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val
        self.theBoardSize = 19
        self.theHandicapPoint = 0

    def className(self):
        return "ConfigClass"

    def goObject(self):
        return self.theGoObject

    def boardSize(self):
        return self.theBoardSize

