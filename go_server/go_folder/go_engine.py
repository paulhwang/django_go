def malloc(go_val):
    return GoEngineClass(go_val)

class GoEngineClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val;
