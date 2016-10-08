def malloc(engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val):
    return GoGroupListClass(engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val)

class GoGroupListClass(object):
    def __init__(self, engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val):
        self.theEngineObject = engine_val;

    def className(self):
        return "GoGroupListClass"

    def engineObject(self):
        return self.theEngineObject

    def goObject(self):
        return self.engineObject().goObject()


