def malloc(go_val):
    return GoHandlerClass(go_val)

class GoHandlerClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val;

    def className(self):
        return "GoHandlerClass"

    def goObject(self):
        return self.theGoObject

    def gameObject(self):
        return self.goObject().gameObject()

    def portObject(self):
        return self.goObject().portObject()

    def aMoveIsPlayed(self, str_val):
        #self.debug(False, "aMoveIsPlayed", str_val);
        if self.gameObject().gameIsOver():
            index = 0
            x = (str_val.charAt(0) - ord('0')) * 10
            x += (str_val.charAt(1) - ord('0'))
            y = (str_val.charAt(2) - ord('0')) * 10
            y += (str_val.charAt(3) - ord('0'))
            if str_val.charAt(4) - ord('0') != self.goObject().MARK_DEAD_STONE_DIFF():
                self.abend("aMoveIsPlayed", "game is over")
                return
            self.engineObject().markDeadGroup(x, y)
            self.engineObject().abendEngine()
            self.portObject().thansmitBoardData()
        else:
            move = self.goObject().mallocMove(str_val, 0, 0, 0, 0, self.goObject())
            self.gameObject().addNewMoveAndFight(move)
            self.portObject().thansmitBoardData()

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

