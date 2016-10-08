def malloc(go_val):
    return BoardClass(go_val)

class BoardClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val
        self.theBoardArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        self.theMarkedBoardArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        i = 0
        while i < 19:
            self.theBoardArray[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
            self.theMarkedBoardArray[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
            i += 1
        self.resetBoardObjectData()

    def resetBoardObjectData(self):
        #self.goLog("resetBoardObjectData", "boardSize=" + self.boardSize())
        i = 0
        while i < self.boardSize():
            j = 0
            while j < self.boardSize():
                self.setBoardArray(i, j, self.goObject().EMPTY_STONE())
                j += 1
            i += 1

    def className(self):
        return "BoardClass"

    def goObject(self):
        return self.theGoObject

    def configObject(self):
        return self.goObject().configObject();

    def boardSize(self):
        return self.configObject().boardSize()

    def setBoardArray(self, x_val, y_val, data_val):
        self.theBoardArray[x_val][y_val] = data_val

    def setMarkedBoardArray(self, x_val, y_val, data_val):
        self.theMarkedBoardArray[x_val][y_val] = data_val

    def resetMarkedBoardObjectData(self):
        i = 0
        while i < self.boardSize():
            j = 0
            while j < self.boardSize():
                self.setMarkedBoardArray(i, j, self.goObject().EMPTY_STONE())
                j += 1
            i += 1


