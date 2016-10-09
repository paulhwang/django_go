import go_server.go_folder.go_config
import go_server.go_folder.go_board
import go_server.go_folder.go_engine
import go_server.go_folder.go_game
import go_server.go_folder.go_port
import go_server.go_folder.go_move

def malloc(root_val):
    return GoClass(root_val)

def malloc_config(go_val):
    return go_server.go_folder.go_config.malloc(go_val)

def malloc_board(go_val):
    return go_server.go_folder.go_board.malloc(go_val)

def malloc_engine(go_val):
    return go_server.go_folder.go_engine.malloc(go_val)

def malloc_game(go_val):
    return go_server.go_folder.go_game.malloc(go_val)

def malloc_port(go_val):
    return go_server.go_folder.go_port.malloc(go_val)

def malloc_move(str_val, x_val, y_val, color_val, turn_val, go_val):
    return go_server.go_folder.go_move.malloc(str_val, x_val, y_val, color_val, turn_val, go_val)

class GoClass(object):
    def __init__(self, root_val):
        self.theRootObject = root_val
        self.theConfigObject = malloc_config(self)
        self.theBoardObject = malloc_board(self)
        self.theEngineObject = malloc_engine(self)
        self.theGameObject = malloc_game(self)
        self.thePortObject = malloc_port(self)

    def className(self):
        return "GoClass"

    def rootObject(self):
        return self.theRootObject

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

    def getOppositeColor(self, color_val):
        if color_val == self.BLACK_STONE():
            return self.WHITE_STONE()

        if color_val == self.WHITE_STONE():
            return self.BLACK_STONE()

        self.abend("getOppositeColor", "color=" + color_val)
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

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().logit(self.className() + "." + str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject.abend(self.className() + "." + str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

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


