def malloc(engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val):
    return GoGroupListClass(engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val)

class GoGroupListClass(object):
    def __init__(self, engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val):
        self.theEngineObject = engine_val
        self.theIndexNumber = index_val
        self.theMyColor = color_val;
        if self.myColor() == self.goObject().EMPTY_STONE():
            self.theHisColor = self.goObject().EMPTY_STONE()
        else:
            self.theHisColor = self.goObject().getOppositeColor(self.myColor())
        self.theIsDead = dead_val
        self.theBigStoneColor = big_stone_val
        self.theSmallStoneColor = small_stone_val
        self.theGroupCount = 0
        self.theIsMarkedDead = 0
        self.theListArray = []

    def className(self):
        return "GoGroupListClass"

    def engineObject(self):
        return self.theEngineObject

    def goObject(self):
        return self.engineObject().goObject()

    def myColor(self):
        return self.theMyColor;

    def hisColor(self):
        return self.theHisColor;

    def groupCount(self):
        return self.theGroupCount;

    def findCandidateGroup(self, x_val, y_val):
        #self.logit("GoGroupListObject.findCandidateGroup", "(" + move_val.xX_() + "," + move_val.yY_() + ")")
        i = 0
        while i < self.groupCount():
            #self.logit("GoGroupListObject.findCandidateGroup", "(" + x_val + "," + y_val + ")")
            if self.listArray(i).isCandidateGroup(x_val, y_val):
                return self.listArray(i)
            i += 1
        #self.logit("GoGroupListObject.findCandidateGroup", "not found")
        return 0

    def findOtherCandidateGroup(self, group_val, x_val, y_val):
        i = 0;
        while i < self.groupCount():
            if self.listArray(i) != group_val:
                if self.listArray(i).isCandidateGroup(x_val, y_val):
                    return self.listArray(i)
            i += 1
        return 0


