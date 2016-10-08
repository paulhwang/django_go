def malloc(group_list_val):
    return GroupClass(group_list_val)

class GroupClass(object):
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

    def createMatrix(self):
        matrix =  [0] * 19
        i = 0
        while i < 19:
            matrix[i] = [0] * 19
            i += 1
        return matrix

    def className(self):
        return "GroupClass"

    def groupListObject(self):
        return self.theGroupListObject

    def setGroupListObject(self, group_list_val):
        self.theGroupListObject = group_list_val

    def goObject(self):
        return self.groupListObject().goObject()

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


