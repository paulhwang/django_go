import go_server.go_folder.go_group_list

def malloc(go_val):
    return GoEngineClass(go_val)

def malloc_group_list(engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val):
    return go_server.go_folder.go_group_list.malloc(engine_val, index_val, color_val, dead_val, big_stone_val, small_stone_val)

class GoEngineClass(object):
    def debugEngine(self):
        return True

    def __init__(self, go_val):
        self.theGoObject = go_val
        self.resetEngineObjectData()

    def resetEngineObjectData(self):
        self.theGroupListArray = [0] * 7
        self.theGroupListArray[1] = malloc_group_list(self, 1, self.goObject().BLACK_STONE(), 0, 0, 0)
        self.theGroupListArray[2] = malloc_group_list(self, 2, self.goObject().WHITE_STONE(), 0, 0, 0)
        self.resetMarkedGroupLists()
        self.resetEmptyGroupLists()

        self.theCaptureCount = 0
        self.theLastDeadStone = 0
        self.theBlackCaptureStones = 0
        self.theWhiteCaptureStones = 0

    def resetMarkedGroupLists(self):
        self.theGroupListArray[3] = malloc_group_list(self, 3, self.goObject().BLACK_STONE(), 1, "black", "gray")
        self.theGroupListArray[4] = malloc_group_list(self, 4, self.goObject().WHITE_STONE(), 1, "white", "gray")
        self.boardObject().resetMarkedBoardObjectData()

    def resetEmptyGroupLists(self):
        self.theGroupListArray[0] = malloc_group_list(self, 0, self.goObject().EMPTY_STONE(), 0, 0, 0)
        self.theGroupListArray[5] = malloc_group_list(self, 5, self.goObject().EMPTY_STONE(), 0, 0, "black")
        self.theGroupListArray[6] = malloc_group_list(self, 6, self.goObject().EMPTY_STONE(), 0, 0, "white")

    def malloc_group_list(self):
        return go_server.go_folder.go_group_lsit.malloc(self)

    def className(self):
        return "GoEngineClass"

    def goObject(self):
        return self.theGoObject

    def boardObject(self):
        return self.goObject().boardObject()

    def configObject(self):
        return self.goObject().configObject()

    def gameObject(self):
        return self.goObject().gameObject()

    def boardSize(self):
        return self.configObject().boardSize()

    def groupListArray(self, index_val):
        return self.theGroupListArray[index_val]

    def emptyGroupList(self):
        return self.theGroupListArray[0]

    def blackGroupList(self):
        return self.theGroupListArray[1]

    def whiteGroupList(self):
        return self.theGroupListArray[2]

    def blackDeadGroupList(self):
        return self.theGroupListArray[3]

    def whiteDeadGroupList(self):
        return self.theGroupListArray[4]

    def blackEmptyGroupList(self):
        return self.theGroupListArray[5]

    def whiteEmptyGroupList(self):
        return self.theGroupListArray[6]

    def lastDeadStone(self):
        return self.theLastDeadStone

    def setLastDeadStone(self, x_val, y_val):
        self.theLastDeadStone = "";
        if x_val < 10:
           self.theLastDeadStone = self.theLastDeadStone + 0
        self.theLastDeadStone = self.theLastDeadStone + x_val

        if y_val < 10:
            self.theLastDeadStone = self.theLastDeadStone + 0
        self.theLastDeadStone = self.theLastDeadStone + y_val

    def clearLastDeadStone(self):
        self.theLastDeadStone = 0

    def enterWar(self, move_val):
        self.logit("enterWar", "(%i,%i) color=%i turn=%i", move_val.xX(), move_val.yY(), move_val.myColor(), move_val.turnIndex())

        group = self.insertStoneToGroupList(move_val)
        self.boardObject().addStoneToBoard(move_val.xX(), move_val.yY(), move_val.myColor())
        dead_count = self.killOtherColorGroups(move_val, group)
        self.logit("enterWar", "dead_count=%i", dead_count)

        if group.groupHasAir() == 0:
            self.removeDeadGroup(group)

        if dead_count != 0:
            if move_val.myColor() == self.GO().BLACK_STONE():
                self.addBlackCaptureStones(dead_count)
            else:
                if move_val.myColor() == self.GO().WHITE_STONE():
                    self.addWhiteCaptureStones(dead_count)
                else:
                    self.goAbend("enterWar", "color=" + move_val.myColor())

        self.abendEngine()

    def insertStoneToGroupList(self, move_val):
        g_list = 0

        if move_val.myColor() == self.goObject().BLACK_STONE():
            g_list = self.blackGroupList()
        else:
            if move_val.myColor() == self.goObject().WHITE_STONE():
                g_list = self.whiteGroupList()
            else:
                self.goAbend("insertStoneToGroupList", "color=" + move_val.myColor())

        group = g_list.findCandidateGroup(move_val.xX(), move_val.yY())
        if group == 0:
            group = g_list.malloc_group()
            group.insertStoneToGroup(move_val.xX(), move_val.yY(), 0)
            g_list.insertGroupToGroupList(group)
            #g_list.printGroupList()
            return group

        group.insertStoneToGroup(move_val.xX(), move_val.yY(), 0)
        #g_list.printGroupList()

        dummy_count = 0
        group2 = 0
        while true:
            group2 = g_list.findOtherCandidateGroup(group, move_val.xX(), move_val.yY())
            if group2 == 0:
                break
            dummy_count += 1
            group.mergeWithOtherGroup(group2)
            g_list.removeGroupFromGroupList(group2)
        if dummy_count > 3:
            self.goAbend("insertStoneToGroupList", "dummy_count")
        return group

    def killOtherColorGroups(self, move_val, group_val):
        self.clearLastDeadStone();
        count = self.killOtherColorGroup(group_val, move_val.xX() - 1, move_val.yY())
        count += self.killOtherColorGroup(group_val, move_val.xX() + 1, move_val.yY())
        count += self.killOtherColorGroup(group_val, move_val.xX(), move_val.yY() - 1)
        count += self.killOtherColorGroup(group_val, move_val.xX(), move_val.yY() + 1)
        return count

    def killOtherColorGroup(self, group, x, y):
        if not self.goObject().isValidCoordinates(x, y, self.boardSize()):
            return 0

        if self.boardObject().boardArray(x, y) != group.hisColor():
            return 0

        his_group = self.getGroupByCoordinate(x, y, group.hisColor())
        if not his_group:
            self.goAbend("killOtherColorGroup", "x=" + x + " y=" + y);
            return 0

        if his_group.groupHasAir():
            return 0

        dead_count = his_group.stoneCount()

        if (group.stoneCount() == 1) and (his_group.stoneCount() == 1):
            self.markLastDeadInfo(his_group)

        self.removeDeadGroup(his_group)
        return dead_count

    def getGroupByCoordinate(self, x_val, y_val, color_val):
        self.debug(False, "GoEngineObject.getGroupByCoordinate", color_val);
        if (color_val == self.goObject().BLACK_STONE()) or (color_val == self.goObject().MARKED_DEAD_BLACK_STONE()):
            g_list = self.blackGroupList()
        else:
            g_list = self.whiteGroupList()

        self.debug(False, "GoEngineObject.getGroupByCoordinate", "groupCount=%i", g_list.groupCount())
        i = 0
        while i < g_list.groupCount():
            self.debug(False, "GoEngineObject.getGroupByCoordinate", "i=%i", i)
            if g_list.listArray(i).existMatrix(x_val, y_val):
                self.debug(False, "GoEngineObject.getGroupByCoordinate", "i=%i", i)
                return g_list.listArray(i)
            i += 1
        return null

    def stoneHasAir(self, x_val, y_val):
        if self.boardObject().isEmptySpace(x_val, y_val - 1):
            return True
        if self.boardObject().isEmptySpace(x_val, y_val + 1):
            return True
        if self.boardObject().isEmptySpace(x_val - 1, y_val):
            return True
        if self.boardObject().isEmptySpace(x_val + 1, y_val):
            return True
        return False

    def abendEngine(self):
        if not self.debugEngine():
            return

        stones_count = 0;
        i = 0;
        while i < 7:
            self.groupListArray(i).abendGroupList()
            stones_count += self.groupListArray(i).totalStoneCount()
            i += 1;

        self.debug(False, "abendEngine", self.gameObject().gameIsOver())
        if self.gameObject().gameIsOver():
            if self.boardSize() * self.boardSize() != stones_count:
                self.abend("abendEngine", "stones_count=%i", stones_count)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.goObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

