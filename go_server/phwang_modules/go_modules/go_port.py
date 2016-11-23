import json

def malloc(base_object_val):
    return GoPortClass(base_object_val)

class GoPortClass(object):
    def __init__(self, base_object_val):
        self.theBaseObject = base_object_val;
        self.GO_PROTOCOL_CODE_SIZE = 7;
        self.GO_PROTOCOL_CODE_PROPOSE = "Propose";
        self.GO_PROTOCOL_CODE_ACCEPT = "Accept ";
        self.GO_PROTOCOL_CODE_CONFIRM = "Confirm";
        self.GO_PROTOCOL_CODE_MOVE_DATA = "Move   ";
        self.GO_PROTOCOL_CODE_SPECIAL_MOVE = "Special";
        self.GO_PROTOCOL_CODE_BOARD_DATA = "Board  ";
        self.debug(False, "init__", "")

    def objectName(self):
        return "GoPortClass"

    def baseObject(self):
        return self.theBaseObject

    def clusterObject(self):
        return self.baseObject().clusterObject()

    def engineObject(self):
        return self.baseObject().engineObject()

    def gameObject(self):
        return self.baseObject().gameObject()

    def boardObject(self):
        return self.baseObject().boardObject()

    def thansmitBoardData(self):
        board_data = self.GO_PROTOCOL_CODE_BOARD_DATA + self.boardObject().encodeBoard();
        self.debug(False, "transmitBoardData", "data=%s", board_data);
        json_data = json.dumps({
                       "board_data": board_data,
                       "next_color": self.gameObject().nextColor(),
                       "last_dead_stone": self.engineObject().lastDeadStone(),
                       "capture_count": self.engineObject().captureCount(),
                       "game_is_over": self.gameObject().gameIsOver(),
                       "black_score": self.engineObject().blackScoreString(),
                       "white_score": self.engineObject().whiteScoreString(),
                       "final_score": self.engineObject().finalScoreString(),
                   });
        self.transmitData(json_data);

    def transmitData(self, data_val):
        if self.baseObject().objectName() == "GoBaseObject":
            return
        self.clusterObject().enqueueTransmitData(data_val)
        self.clusterObject().processTransmitData()

    def receiveStringData(self, str_val):
        self.debug(False, "receiveStringData", str_val)
        if str_val == None:
            self.abend("receiveStringData", "null input");
            return

        code = str_val[:self.GO_PROTOCOL_CODE_SIZE]
        data = str_val[self.GO_PROTOCOL_CODE_SIZE:]
        self.debug(False, "receiveStringData", "code=%s", code)
        self.debug(False, "receiveStringData", "data=%s", data)

        if code == self.GO_PROTOCOL_CODE_MOVE_DATA:
            self.aMoveIsPlayed(data)
            return

        if code == self.GO_PROTOCOL_CODE_SPECIAL_MOVE:
            self.aSpecialMoveIsPlayed(data)
            return

    def aMoveIsPlayed(self, str_val):
        self.debug(False, "aMoveIsPlayed", str_val);
        if self.gameObject().gameIsOver():
            index = 0
            x = (str_val.charAt(0) - ord('0')) * 10
            x += (str_val.charAt(1) - ord('0'))
            y = (str_val.charAt(2) - ord('0')) * 10
            y += (str_val.charAt(3) - ord('0'))
            if str_val.charAt(4) - ord('0') != self.baseObject().MARK_DEAD_STONE_DIFF():
                self.abend("aMoveIsPlayed", "game is over")
                return
            self.engineObject().markDeadGroup(x, y)
            self.engineObject().abendEngine()
            self.thansmitBoardData()
        else:
            move = self.baseObject().mallocMove(str_val, 0, 0, 0, 0, self.baseObject())
            self.gameObject().addNewMoveAndFight(move)
            self.thansmitBoardData()

    def aSpecialMoveIsPlayed(self, str_val):
        self.debug(False, "aSpecialMoveIsPlayed", str_val)
        self.gameObject().receiveSpecialMoveFromOpponent(str_val)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.baseObject().logit(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.baseObject().abend(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

