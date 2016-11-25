def malloc(root_object_val, base_id_val):
    return GoBaseObject(root_object_val, base_id_val)

class GoBaseObject(object):
    def __init__(self, root_object_val, base_id_val):
        self.theRootObject = root_object_val;
        self.theJointObject = self.rootObject().importObject().importListMgr().malloc_joint(base_id_val)
        self.theConfigObject = self.rootObject().importObject().importConfig().malloc(self)
        self.theBoardObject = self.rootObject().importObject().importBoard().malloc(self)
        self.theEngineObject = self.rootObject().importObject().importEngine().malloc(self)
        self.theGameObject = self.rootObject().importObject().importGame().malloc(self)
        self.thePortObject = self.rootObject().importObject().importPort().malloc(self)
        self.debug(True, "init__", "baseId=%d", self.baseId())

    def objectName(self):
        return "GoBaseObject"

    def rootObject(self):
        return self.theRootObject

    def jointObject(self):
        return self.theJointObject

    def configObject(self):
        return self.theConfigObject

    def boardObject(self):
        return self.theBoardObject

    def engineObject(self):
        return self.theEngineObject

    def gameObject(self):
        return self.theGameObject

    def portObject(self):
        return self.thePortObject

    def baseId(self):
        return self.jointObject().entryId()

    def getOppositeColor(self, color_val):
        if color_val == self.BLACK_STONE():
            return self.WHITE_STONE()

        if color_val == self.WHITE_STONE():
            return self.BLACK_STONE()

        self.abend("getOppositeColor", "color=%i", color_val)
        return self.EMPTY_STONE()

    def isNeighborStone(self, x1_val, y1_val, x2_val, y2_val):
        if x1_val == x2_val:
            if (y1_val + 1 == y2_val) or (y1_val - 1 == y2_val):
                return True
        if y1_val == y2_val:
            if (x1_val + 1 == x2_val) or (x1_val - 1 == x2_val):
                return True
        return False

    def isValidCoordinates(self, x_val, y_val, board_size_val):
        return self.isValidCoordinate(x_val, board_size_val) and self.isValidCoordinate(y_val, board_size_val)

    def isValidCoordinate(self, coordinate_val, board_size_val):
        return (0 <= coordinate_val) and (coordinate_val < board_size_val)

    def mallocMove(self, str_val, x_val, y_val, color_val, turn_val, go_val):
        return self.rootObject().importObject().importMove().malloc(str_val, x_val, y_val, color_val, turn_val, go_val)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def LOG_IT(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(str(self.baseId()) + ":" + str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def ABEND(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(str(self.baseId()) + ":" + str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def EMPTY_STONE(self):
        return 0

    def BLACK_STONE(self):
        return 1

    def WHITE_STONE(self):
        return 2

    def MARK_DEAD_STONE_DIFF(self):
        return 4

    def MARK_EMPTY_STONE_DIFF(self):
        return 6

    def MARKED_DEAD_BLACK_STONE(self):
        return self.BLACK_STONE() + self.MARK_DEAD_STONE_DIFF()

    def MARKED_DEAD_WHITE_STONE(self):
        return self.WHITE_STONE() + self.MARK_DEAD_STONE_DIFF()


