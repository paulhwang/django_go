def malloc(go_val):
    return GoGameClass(go_val)

class GoGameClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val
        self.resetGameObjectData()

    def resetGameObjectData(self):
        self.theMaxMove = 0
        self.theTotalMoves = 0
        self.theMovesArray = []
        self.resetGameObjectPartialData()

    def resetGameObjectPartialData(self):
        self.theNextColor = self.goObject().BLACK_STONE()
        self.thePassReceived = 0
        self.theGameIsOver = 0

    def className(self):
        return "GoGameClass"

    def goObject(self):
        return self.theGoObject

    def passReceived(self):
        return self.thePassReceived

    def maxMove(self):
        return self.theMaxMove

    def setMaxMove(self, max_move_val):
        self.theMaxMove = max_move_val

    def totalMoves(self):
        return self.theTotalMoves

    def setTotalMoves(self, total_moves_val):
        self.theTotalMoves = total_moves_val

    def incrementTotalMoves(self):
        self.theTotalMoves += 1

    def decrementTotalMoves(self):
        self.theTotalMoves -= 1

    def nextColor(self):
        return self.theNextColor

    def setNextColor(self, next_color_val):
        self.theNextColor = next_color_val;

    def setPassReceived(self):
        self.thePassReceived = 1

    def clearPassReceived(self):
        self.thePassReceived = 0

    def gameIsOver(self):
        return self.theGameIsOver

    def setGameIsOver(self):
        self.theGameIsOver = 1

    def clearGameIsOver(self):
        self.theGameIsOver = 0

    def addNewMoveAndFight(self, move_val):
        self.debug(1, "addNewMoveAndFight", "")

        if self.gameIsOver():
            self.goLog("addNewMoveAndFight", "two pass have entered")
            return

        self.clearPassReceived()
        self.insertMoveToMoveList(move_val)
        #self.engineObject().enterWar(move_val)
        self.setNextColor(self.goObject().getOppositeColor(move_val.myColor()))

    def insertMoveToMoveList(self, move_val):
        #self.setMovesArray(self.totalMoves(), move_val)
        self.incrementTotalMoves()
        self.setMaxMove(self.totalMoves())

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val != 0:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().logit(self.className() + "." + str1 + "() " + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().abend(self.className() + "." + str1 + "() " + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

