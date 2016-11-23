import go_server.phwang_modules.go_modules.go_config
import go_server.phwang_modules.go_modules.go_board
import go_server.phwang_modules.go_modules.go_engine
import go_server.phwang_modules.go_modules.go_game
import go_server.phwang_modules.go_modules.go_port
import go_server.phwang_modules.go_modules.go_move

def malloc(base_mgr_object_val):
    return GoBaseObject(base_mgr_object_val)

def malloc_config(go_val):
    return go_server.phwang_modules.go_modules.go_config.malloc(go_val)

def malloc_board(go_val):
    return go_server.phwang_modules.go_modules.go_board.malloc(go_val)

def malloc_engine(go_val):
    return go_server.phwang_modules.go_modules.go_engine.malloc(go_val)

def malloc_game(go_val):
    return go_server.phwang_modules.go_modules.go_game.malloc(go_val)

def malloc_port(go_val):
    return go_server.phwang_modules.go_modules.go_port.malloc(go_val)

def malloc_move(str_val, x_val, y_val, color_val, turn_val, go_val):
    return go_server.phwang_modules.go_modules.go_move.malloc(str_val, x_val, y_val, color_val, turn_val, go_val)

class GoBaseObject(object):
    def __init__(self, base_mgr_object_val):
        self.theBaseMgrObject = base_mgr_object_val;
        self.theConfigObject = malloc_config(self)
        self.theBoardObject = malloc_board(self)
        self.theEngineObject = malloc_engine(self)
        self.theGameObject = malloc_game(self)
        self.thePortObject = malloc_port(self)
        self.theBaseId = self.baseMgrObject().globalBaseId()
        self.thePrev = None
        self.theNext = None
        self.debug(True, "init__", "")

    def objectName(self):
        return "GoBaseObject"

    def baseMgrObject(self):
        return self.theBaseMgrObject

    def goRootObject(self):
        return self.baseMgrObject().goRootObject()

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
        return "123456"

    def prev(self):
        return self.thePrev

    def setPrev(self, val):
        self.thePrev = val

    def next(self):
        return self.theNext

    def setNext(self, val):
        self.theNext = val

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
        return malloc_move(str_val, x_val, y_val, color_val, turn_val, go_val)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goLogit(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goAbend(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def goLogit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goRootObject().LOG_IT(self.baseId() + " " + str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def goAbend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goRootObject().ABEND(self.baseId() + " " + str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

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

