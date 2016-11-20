def malloc(group_list_val):
    return GroupClass(group_list_val)

class GroupClass(object):
    def debugGroup(self):
        return True

    def __init__(self, group_list_val):
        self.theGroupListObject = group_list_val
        self.theIndexNumber = self.groupListObject().groupCount();
        self.theMyColor = self.groupListObject().myColor();
        if self.myColor() == self.goObject().EMPTY_STONE():
            self.theHisColor = self.goObject().EMPTY_STONE()
        else:
            self.theHisColor = self.goObject().getOppositeColor(self.myColor());
        self.theStoneCount = 0;
        self.theExistMatrix = self.createMatrix();
        self.theDeadMatrix = self.createMatrix();
        self.debug(False, "init__", "")

    def createMatrix(self):
        matrix =  [0] * 19
        i = 0
        while i < 19:
            matrix[i] = [0] * 19
            i += 1
        return matrix

    def objectName(self):
        return "GroupClass"

    def groupListObject(self):
        return self.theGroupListObject

    def setGroupListObject(self, group_list_val):
        self.theGroupListObject = group_list_val

    def engineObject(self):
        return self.groupListObject().engineObject()

    def goObject(self):
        return self.engineObject().goObject()

    def boardObject(self):
        return self.goObject().boardObject()

    def configObject(self):
        return self.goObject().configObject()

    def boardSize(self):
        return self.configObject().boardSize()

    def indexNumber(self):
        return self.theIndexNumber;

    def setIndexNumber(self, val):
        self.theIndexNumber = val;

    def myColor(self):
        return self.theMyColor;

    def hisColor(self):
        return self.theHisColor;

    def stoneCount(self):
        return self.theStoneCount;

    def incrementStoneCount(self):
        self.theStoneCount += 1;

    def decrementStoneCount(self):
        self.theStoneCount -= 1;

    def maxX(self):
        return self.theMaxX;

    def minX(self):
        return self.theMinX;

    def maxY(self):
        return self.theMaxY;

    def minY(self):
        return self.theMinY;

    def setMaxX(self, val):
        self.theMaxX = val;

    def setMinX(self, val):
        self.theMinX = val;

    def setMaxY(self, val):
        self.theMaxY = val;

    def setMinY(self, val):
        self.theMinY = val;

    def existMatrix(self, x_val, y_val):
        return self.theExistMatrix[x_val][y_val];

    def deadMatrix(self, x_val, y_val):
        return self.theDeadMatrix[x_val][y_val];

    def setExistMatrix(self, x_val, y_val, data_val):
        self.theExistMatrix[x_val][y_val] = data_val;
        #self.printGroup();

    def setDeadMatrix(self, x_val, y_val, data_val):
        self.theDeadMatrix[x_val][y_val] = data_val;

    def insertStoneToGroup(self, x_val, y_val, dead_val):
        #GO.self.logit("GoGroupObject.insertStoneToGroup", "x=" + x_val + " y=" + y_val + " color=" + self.myColor_())
        if self.existMatrix(x_val, y_val):
            self.GO().goAbend("insert_stone", "x=" + x_val + " y=" + y_val + " color=" + self.myColor())

        if self.stoneCount() == 0:
            self.setMaxX(x_val)
            self.setMinX(x_val)
            self.setMaxY(y_val)
            self.setMinY(y_val)
        else:
            if x_val > self.maxX():
                self.setMaxX(x_val)
            if x_val < self.minX():
                self.setMinX(x_val)
            if y_val > self.maxY():
                self.setMaxY(y_val)
            if y_val < self.minY():
                self.setMinY(y_val)

        self.incrementStoneCount()
        self.setExistMatrix(x_val, y_val, 1)
        self.setDeadMatrix(x_val, y_val, dead_val)

    def isCandidateGroup(self, x_val, y_val):
        #self.debug(False, "isCandidateGroup", "(%i,%i)" + x_val, y_val)
        i = self.minX()
        while i <=  self.maxX():
            j = self.minY()
            while j <= self.maxY():
                if self.existMatrix(i, j):
                    #goObject().goLog("isCandidateGroup", "(%i,%i) (%i,%i)", x_val, y_val, i, j)
                    if self.goObject().isNeighborStone(i, j, x_val, y_val):
                        return True
                j += 1
            i += 1
        return False

    def mergeWithOtherGroup(self, group2):
        self.debug(False, "mergeWithOtherGroup", "");
        #self.debugGroupObject();
        i = group2.minX();
        while i <= group2.maxX():
            j = group2.minY();
            while j <= group2.maxY():
                if group2.existMatrix(i, j):
                    self.debug(False, "mergeWithOtherGroup", "i=%i j=%i", i, j);
                    if self.existMatrix(i, j):
                        Go.abend("goMergeWithOtherGroup", "already exist");
                    self.setExistMatrix(i, j, group2.existMatrix(i, j));
                    self.incrementStoneCount();

                    group2.setExistMatrix(i, j, False);
                    group2.decrementStoneCount();
                j += 1;
            i += 1;
        #self.debugGroupObject();

        if self.maxX() < group2.maxX():
            self.setMaxX(group2.maxX());
        if self.minX() > group2.minX():
            self.setMinX(group2.minX());
        if self.maxY() < group2.maxY():
            self.setMaxY(group2.maxY());
        if self.minY() > group2.minY():
            self.setMinY(group2.minY());

        if group2.groupListObject().listArray(group2.indexNumber()) != group2:
            self.abend("merge_with_other_group", "group2");

    def groupHasAir(self):
        #self.logit("groupHasAir", "color=" + self.myColor_() + " count=" + self.stoneCount_());
        i = self.minX()
        while i <= self.maxX():
            j = self.minY()
            while j <= self.maxY():
                #self.logit("groupHasAir", "(" + i + "," + j + ")")
                if self.existMatrix(i, j):
                    #self.logit("groupHasAir", "(" + i + "," + j + ")")
                    if self.engineObject().stoneHasAir(i, j):
                        #self.logit("groupHasAir", "(" + i + "," + j + ")")
                        return True
                j += 1
            i += 1
        return False

    def removeDeadStoneFromBoard(self):
        i = self.minX();
        while i <= self.maxX():
            j = self.minY();
            while j <= self.maxY():
                if self.existMatrix(i, j):
                    self.boardObject().setBoardArray(i, j, self.goObject().EMPTY_STONE());
                    self.debug(False, "removeDeadStoneFromBoard", "(%i,%i)", i, j);
                j += 1;
            i += 1;

    def abendGroup(self):
        if not self.debugGroup():
            return

        self.debug(False, "abendGroup", "color=%i count=%i index=%i", self.myColor(), self.stoneCount(), self.indexNumber())
        count = 0

        i = 0
        while i < self.boardSize():
            j = 0
            while j < self.boardSize():
                if self.existMatrix(i, j):
                    #self.logit("abendGroup", "(" + i + "," + j + ") color=" + self.myColor())
                    count += 1
                j += 1
            i += 1
        #self.logit("abendGroup", self.stoneCount_() + "==" + count)
        if self.stoneCount() != count:
            self.printGroup()
            self.abend("abendGroup", self.stoneCount() + "!=" + count)
        #self.printGroup()

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().logit(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().abend(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)



