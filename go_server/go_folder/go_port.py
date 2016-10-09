def malloc(go_val):
    return GoPortClass(go_val)

class GoPortClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val;

    def className(self):
        return "GoPortClass"

    def goObject(self):
        return self.theGoObject

    def handlerObject(self):
        return self.goObject().handlerObject()

    def gameObject(self):
        return self.goObject().gameObject()

    def thansmitBoardData(self):
        #board_data = self.GO_PROTOCOL_CODE_BOARD_DATA + self.boardObject().encodeBoard();
        self.debug(True, "transmitBoardData", "data=%s", "board_data");
        #json_data = JSON.stringify({
        #               board_data: board_data,
        #               next_color: self.gameObject().nextColor(),
        #               last_dead_stone: self.engineObject().lastDeadStone(),
        #               capture_count: self.engineObject().captureCount(),
        #               game_is_over: self.gameObject().gameIsOver(),
        #               black_score: self.engineObject().blackScoreString(),
        #               white_score: self.engineObject().whiteScoreString(),
        #               final_score: self.engineObject().finalScoreString(),
        #           });
        #self.transmitData(json_data);

    def receiveStringData(self, str_val):
        self.logit("receiveStringData", str_val)
        if str_val == None:
            self.abend("receiveStringData", "null input");
            return

        self.handlerObject().aMoveIsPlayed(str_val)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

