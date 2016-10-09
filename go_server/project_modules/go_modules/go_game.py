def malloc(go_val):
    return GoGameClass(go_val)

class GoGameClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val
        self.resetGameObjectData()

    def resetGameObjectData(self):
        self.theMaxMove = 0
        self.theTotalMoves = 0
        self.theMovesArray = [None] * 400
        self.resetGameObjectPartialData()

    def resetGameObjectPartialData(self):
        self.theNextColor = self.goObject().BLACK_STONE()
        self.thePassReceived = False
        self.theGameIsOver = False

    def className(self):
        return "GoGameClass"

    def goObject(self):
        return self.theGoObject

    def engineObject(self):
        return self.goObject().engineObject()

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

    def movesArray(self, i):
        return self.theMovesArray[i]

    def setMovesArray(self, i, val):
        self.theMovesArray[i] = val

    def nextColor(self):
        return self.theNextColor

    def setNextColor(self, next_color_val):
        self.theNextColor = next_color_val;

    def setPassReceived(self):
        self.thePassReceived = True

    def clearPassReceived(self):
        self.thePassReceived = False

    def gameIsOver(self):
        return self.theGameIsOver

    def setGameIsOver(self):
        self.theGameIsOver = True

    def clearGameIsOver(self):
        self.theGameIsOver = False

    def addNewMoveAndFight(self, move_val):
        self.debug(False, "addNewMoveAndFight", "")

        if self.gameIsOver():
            self.debug(True, "addNewMoveAndFight", "two pass have entered")
            return

        self.clearPassReceived()
        self.insertMoveToMoveList(move_val)
        self.engineObject().enterWar(move_val)
        self.setNextColor(self.goObject().getOppositeColor(move_val.myColor()))

    def insertMoveToMoveList(self, move_val):
        self.setMovesArray(self.totalMoves(), move_val)
        self.incrementTotalMoves()
        self.setMaxMove(self.totalMoves())

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
