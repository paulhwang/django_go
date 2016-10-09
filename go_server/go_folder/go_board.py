def malloc(go_val):
    return BoardClass(go_val)

class BoardClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val
        self.theBoardArray = [0] * 19
        self.theMarkedBoardArray = [0] * 19
        i = 0
        while i < 19:
            self.theBoardArray[i] = [0] * 19
            self.theMarkedBoardArray[i] = [0] * 19
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

    def boardArray(self, x_val, y_val):
        return self.theBoardArray[x_val][y_val];

    def markedBoardArray(self, x_val, y_val):
        return self.theMarkedBoardArray[x_val][y_val];

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

    def addStoneToBoard(self, x_val, y_val, color_val):
        if self.goObject().isValidCoordinates(x_val, y_val, self.configObject().boardSize()) == 0:
            self.goAbend("addStoneToBoard", "x=" + x_val + " y=" + y_val)
            return
        self.setBoardArray(x_val, y_val, color_val)

    def isEmptySpace(self, x_val, y_val):
        if not self.goObject().isValidCoordinates(x_val, y_val, self.configObject().boardSize()):
            return False
        if self.boardArray(x_val, y_val) != self.goObject().EMPTY_STONE():
            return False
        return True

    def encodeBoard(self):
        buf = ""
        i = 0
        while i < self.boardSize():
            j = 0
            while j < self.boardSize():
                buf = buf + str(self.theBoardArray[i][j])
                j += 1
            i += 1
        self.logit("encodeBoard", "data=" + buf)
        return buf

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)







