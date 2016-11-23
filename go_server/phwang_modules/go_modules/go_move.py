def malloc(str_val, x_val, y_val, color_val, turn_val, base_object_val):
    return GoMoveClass(str_val, x_val, y_val, color_val, turn_val, base_object_val)

class GoMoveClass(object):
    def __init__(self, str_val, x_val, y_val, color_val, turn_val, base_object_val):
        self.theBaseObject = base_object_val;

        if not str_val:
            self.theX = x_val
            self.theY = y_val
            self.theMyColor = color_val
            self.theTurnIndex = turn_val
        else:
            self.moveObjectDecode(str_val)
        self.debug(True, "init__", "(%d,%d) color=%d turn=%d", self.xX(), self.yY(), self.myColor(), self.turnIndex())

    def objectName(self):
        return "GoMoveClass"

    def baseObject(self):
        return self.theBaseObject

    def xX(self):
        return self.theX;

    def yY(self):
        return self.theY;

    def myColor(self):
        return self.theMyColor;

    def turnIndex(self):
        return self.theTurnIndex

    def moveObjectDecode(self, str_val):
        self.debug(False, "moveObjectDecode", "input=" + str_val)
        self.theX = (ord(str_val[0]) - ord('0')) * 10
        self.theX += ord(str_val[1]) - ord('0')
        self.theY = (ord(str_val[2]) - ord('0')) * 10
        self.theY += ord(str_val[3]) - ord('0')
        self.theMyColor = ord(str_val[4]) - ord('0')
        self.theTurnIndex = (ord(str_val[5]) - ord('0')) * 100
        self.theTurnIndex += (ord(str_val[6]) - ord('0')) * 10
        self.theTurnIndex += ord(str_val[7]) - ord('0')
        self.debug(False, "moveObjectDecode", "(%i,%i)", self.xX(), self.yY())

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.baseObject().logit(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.baseObject().abend(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)


