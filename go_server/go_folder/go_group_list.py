import go_server.go_folder.go_group

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

    def malloc_group(self):
        return go_server.go_folder.go_group.malloc(self)

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

    def listArray(self, index_val):
        return self.theListArray[index_val]

    def setListArray(self, index_val, data_val):
        self.theListArray[index_val] = data_val

    def incrementGroupCount(self):
        self.theGroupCount += 1

    def decrementGroupCount(self):
        self.theGroupCount -= 1

    def insertGroupToGroupList(self, group_val):
        self.setListArray(self.groupCount(), group_val)
        group_val.setIndexNumber(self.groupCount())
        self.incrementGroupCount()
        group_val.setGroupListObject(self)

    def removeGroupFromGroupList(self, group_val):
        self.decrementGroupCount()

        if group_val.indexNumber() != self.groupCount():
            self.listArray(self.groupCount()).setIndexNumber(group_val.indexNumber())
            self.setListArray(group_val.indexNumber(), self.listArray(self.groupCount()))

        self.setListArray(self.groupCount(), null)

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


