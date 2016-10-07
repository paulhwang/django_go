import go_server.go_folder.go_engine
import go_server.go_folder.go_game
import go_server.go_folder.go_port
import go_server.go_folder.go_move

def malloc(root_val):
    return GoClass(root_val)

class GoClass(object):
    def __init__(self, root_val):
        self.theRootObject = root_val
        self.theEngineObject = go_server.go_folder.go_engine.malloc(self)
        self.theGameObject = go_server.go_folder.go_game.malloc(self)
        self.thePortObject = go_server.go_folder.go_port.malloc(self)

    def className(self):
        return "GoClass"

    def rootObject(self):
        return self.theRootObject

    def engineObject(self):
        return self.theEngineObject

    def gameObject(self):
        return self.theGameObject

    def portObject(self):
        return self.thePortObject

    def EMPTY_STONE(self):
        return 0

    def BLACK_STONE(self):
        return 1

    def WHITE_STONE(self):
        return 2

    def getOppositeColor(self, color_val):
        if color_val == self.BLACK_STONE():
            return self.WHITE_STONE()

        if color_val == self.WHITE_STONE():
            return self.BLACK_STONE()

        self.abend("getOppositeColor", "color=" + color_val)
        return self.EMPTY_STONE()

    def mallocMove(self, str_val, x_val, y_val, color_val, turn_val, go_val):
        return  go_server.go_folder.go_move.malloc(str_val, x_val, y_val, color_val, turn_val, go_val)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().logit(self.className() + "." + str1 + "() " + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject.abend(self.className() + "." + str1 + "() " + str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
