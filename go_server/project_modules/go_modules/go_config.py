import json

def malloc(go_val):
    return ConfigClass(go_val)

class ConfigClass(object):
    def __init__(self, go_val):
        self.theGoObject = go_val
        self.theBoardSize = 19
        self.theHandicapPoint = 0

    def className(self):
        return "ConfigClass"

    def goObject(self):
        return self.theGoObject

    def boardSize(self):
        return self.theBoardSize

    def boardSize(self):
        return self.theBoardSize;

    def setBoardSize(self, val):
        self.theBoardSize = val

    def myColor(self):
        return self.theMyColor

    def hisColor(self):
        if self.theMyColor == GO.BLACK_STONE():
            return GO.WHITE_STONE()
        else:
            return GO.BLACK_STONE()

    def setMyColor(self, val):
        if val == "black":
            self.theMyColor = GO.BLACK_STONE()
            return
        if val == "white":
            self.theMyColor = GO.WHITE_STONE()
            return
        self.abend("setMyColor", val)

    def setMyColor_(self, val):
        self.theMyColor = val

    def handicapPoint(self):
        return self.theHandicapPoint

    def setHandicapPoint(self, val):
        self.theHandicapPoint = val

    def komiPoint(self):
        return self.theKomiPoint

    def setKomiPoint(self, val):
        self.theKomiPoint = val

    def createConfig(self, json_data_val):
        self.debug(True, "creataConfig", "data=%s", json_data_val)
        config_data = json.loads(json_data_val)
        self.setBoardSize(config_data.get("board_size"))
        self.setMyColor_(config_data.get("color"))
        self.setKomiPoint(config_data.get("komi"))
        self.setHandicapPoint(config_data.get("handicap"))

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)


