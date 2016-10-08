import go_server.go_folder.go_group

def malloc(engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val):
    return GoGroupListClass(engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val)

class GoGroupListClass(object):
    def debugGroutList(self):
        return True

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
        self.theListArray = [0] * 361

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

    def indexNumber(self):
        return self.theIndexNumber

    def isDead(self):
        return self.theIsDead;

    def groupCount(self):
        return self.theGroupCount;

    def totalStoneCount(self):
        count = 0
        i = 0
        while i < self.groupCount():
            count += self.listArray(i).stoneCount()
            i += 1
        return count

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
        #self.debug(False, "findCandidateGroup", "(" + move_val.xX_() + "," + move_val.yY_() + ")")
        i = 0
        while i < self.groupCount():
            #self.debug(False, "findCandidateGroup", "(" + x_val + "," + y_val + ")")
            if self.listArray(i).isCandidateGroup(x_val, y_val):
                return self.listArray(i)
            i += 1
        self.debug(False, "findCandidateGroup", "not found")
        return 0

    def findOtherCandidateGroup(self, group_val, x_val, y_val):
        i = 0;
        while i < self.groupCount():
            if self.listArray(i) != group_val:
                if self.listArray(i).isCandidateGroup(x_val, y_val):
                    return self.listArray(i)
            i += 1
        return 0

    def abendGroupList(self):
        if not self.debugGroutList():
            return

        if self.isDead():
            d = "d* "
        else:
            d = "*"

        self.debug(False, "abendGroupList", "%i color=%i count=%i:%i", self.indexNumber(), self.myColor(), self.groupCount(), self.totalStoneCount());
        i = 0
        while i < self.groupCount():
            if not self.listArray(i):
                self.goAbend("abendGroupList", "null group " + self.groupCount() + " " + i)
                return
            if self.listArray(i).groupListObject() != self:
                self.abend("abendGroupList", "groupListObject")
                return
            if self.listArray(i).indexNumber() != i:
                self.abend("abendGroupList", "index " + self.listArray(i).indexNumber() + "!=" + i)
                return
            self.listArray(i).abendGroup()
            i += 1

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)



