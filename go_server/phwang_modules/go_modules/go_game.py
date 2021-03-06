def malloc(base_object_val):
    return GoGameClass(base_object_val)

class GoGameClass(object):
    def __init__(self, base_object_val):
        self.theBaseObject = base_object_val
        self.resetGameObjectData()
        self.debug(False, "init__", "")

    def resetGameObjectData(self):
        self.theMaxMove = 0
        self.theTotalMoves = 0
        self.theMovesArray = [None] * 400
        self.resetGameObjectPartialData()

    def resetGameObjectPartialData(self):
        self.theNextColor = self.baseObject().BLACK_STONE()
        self.thePassReceived = False
        self.theGameIsOver = False

    def objectName(self):
        return "GoGameClass"

    def baseObject(self):
        return self.theBaseObject

    def engineObject(self):
        return self.baseObject().engineObject()

    def configObject(self):
        return self.baseObject().configObject()

    def boardObject(self):
        return self.baseObject().boardObject()

    def portObject(self):
        return self.baseObject().portObject()

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
        self.debug(False, "addNewMoveAndFight", "(%i,%i)", move_val.xX(), move_val.yY())

        if self.gameIsOver():
            self.debug(True, "addNewMoveAndFight", "two pass have entered")
            return

        self.clearPassReceived()
        self.insertMoveToMoveList(move_val)
        self.engineObject().enterWar(move_val)
        self.setNextColor(self.baseObject().getOppositeColor(move_val.myColor()))

    def insertMoveToMoveList(self, move_val):
        self.setMovesArray(self.totalMoves(), move_val)
        self.incrementTotalMoves()
        self.setMaxMove(self.totalMoves())

    def FORWARD_MOVE(self):
        return "FORWARD"

    def BACKWARD_MOVE(self):
        return "BACKWARD"

    def DOUBLE_FORWARD_MOVE(self):
        return "DOUBLE_FORWARD"

    def DOUBLE_BACKWARD_MOVE(self):
        return "DOUBLE_BACKWARD"

    def PASS_MOVE(self):
        return "PASS"

    def RESIGN_MOVE(self):
        return "RESIGN"

    def BACK_TO_PLAY_MOVE(self):
        return "BACK_TO_PLAY"

    def CONFIRM_MOVE(self):
        return "CONFIRM"

    def PLAY_ANOTHER_GAME_MOVE(self):
        return "PLAY_ANOTHER_GAME"

    def receiveSpecialMoveFromOpponent(self, data_val):
        self.debug(True, "receiveSpecialMoveFromOpponent", data_val)
        if data_val == self.FORWARD_MOVE():
            self.processForwardMove()
            self.portObject().thansmitBoardData()
            return
        if data_val == self.DOUBLE_FORWARD_MOVE():
            self.processDoubleForwardMove()
            self.portObject().thansmitBoardData()
            return
        if data_val == self.BACKWARD_MOVE():
            self.processBackwardMove()
            self.portObject().thansmitBoardData()
            return
        if data_val == self.DOUBLE_BACKWARD_MOVE():
            self.processDoubleBackwardMove()
            self.portObject().thansmitBoardData()
            return
        if data_val == self.PASS_MOVE():
            self.processPassMove()
            self.portObject().thansmitBoardData()
            return
        if data_val == self.RESIGN_MOVE():
            self.processResignMove()
            return
        if data_val == self.BACK_TO_PLAY_MOVE():
            self.processBackToPlayMove()
            return
        if data_val == self.CONFIRM_MOVE():
            self.processConfirmMove()
            self.portObject().thansmitBoardData()
            return
        if data_val == self.PLAY_ANOTHER_GAME_MOVE():
            self.processPlayAnotherGameMove()
            return

    def processDoubleBackwardMove(self):
        self.debug(False, "processDoubleBackwardMove", "")
        self.clearPassReceived()
        if self.totalMoves() <= self.configObject().handicapPoint():
            return
        self.setTotalMoves(self.configObject().handicapPoint())
        self.processTheWholeMoveList()

    def processBackwardMove(self):
        self.debug(True, "processBackwardMove", "")
        self.clearPassReceived();
        if self.totalMoves() <= self.configObject().handicapPoint():
            return
        self.decrementTotalMoves()
        self.processTheWholeMoveList()

    def processForwardMove(self):
        self.clearPassReceived()
        if self.totalMoves() > self.maxMove():
            self.abend("processForwardMove", "totalMoves=" + self.totalMoves_() + " maxMove=" + self.naxMove_())
            return
        if self.totalMoves() == self.maxMove():
            return
        self.incrementTotalMoves()
        self.processTheWholeMoveList()

    def processDoubleForwardMove(self):
        self.clearPassReceived()
        if self.totalMoves() > self.maxMove():
            self.abend("processDoubleForwardMove", "totalMoves=" + self.totalMoves() + " maxMove=" + self.maxMove_())
            return
        if self.totalMoves() == self.maxMove():
            return
        self.setTotalMoves(self.maxMove())
        self.processTheWholeMoveList()

    def processPassMove(self):
        self.debug(True, "processPassMove", "")

        if not self.passReceived():
            self.setPassReceived()
            self.setNextColor(self.baseObject().getOppositeColor(self.nextColor()))
            return

        self.setGameIsOver()

        self.engineObject().resetMarkedGroupLists()
        self.displayResult();
        self.debug(True, "processPassMove", "game is over")
        ##############self.engineObject().computeScore()
        #################self.engineObject().printScore()
        #################self.engineObject().abendEngine()

    def displayResult(self):
        self.debug(True, "displayResult", "Black: %i (%i + %i + %i*2)" %(self.engineObject().blackScore(), self.engineObject().blackCaptureStones(), self.engineObject().blackLandScore(), self.engineObject().whiteDeadGroupList().totalStoneCount()))
        self.debug(True, "displayResult", "White: %i (%i + %i + %i*2)" %(self.engineObject().whiteScore(), self.engineObject().whiteCaptureStones(), self.engineObject().whiteLandScore(), self.engineObject().blackDeadGroupList().totalStoneCount()))

    def processTheWholeMoveList(self):
        self.boardObject().resetBoardObjectData()
        self.engineObject().resetEngineObjectData()
        self.resetGameObjectPartialData()

        self.debug(True, "processTheWholeMoveLst", "totalMoves=%i", self.totalMoves())
        i = 0
        while i < self.totalMoves():
            move = self.movesArray(i)
            self.engineObject().enterWar(move)
            self.setNextColor(self.baseObject().getOppositeColor(move.myColor()))
            i += 1

    def resetGameObjectPartialData(self):
        self.theNextColor = self.baseObject().BLACK_STONE()
        self.thePassReceived = False
        self.theGameIsOver = False

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.baseObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.baseObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
