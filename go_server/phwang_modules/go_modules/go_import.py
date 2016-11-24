import go_server.phwang_modules.util_modules.logit
import go_server.phwang_modules.util_modules.list_mgr
import go_server.phwang_modules.go_modules.go_base

def malloc(root_object_val):
    return ImportObject(root_object_val)

class ImportObject (object):
    def __init__(self, root_object_val):
        self.theRootObject = root_object_val

    def rootObject(self):
        return self.theRootObject

    def importBase(self):
        return go_server.phwang_modules.go_modules.go_base

    def importConfig(self):
        return require("./go_config.js");

    def importMove(self):
        return require("./go_move.js");

    def importBoard(self):
        return require("./go_board.js");

    def importGame(self):
        return require("./go_game.js");

    def importPort(self):
        return require("./go_port.js");

    def importEngine(self):
        return require("./go_engine.js");

    def importGroup(self):
        return require("./go_group.js");

    def importGroupList(self):
        return require("./go_group_list.js");

    def importListMgr(self):
        return go_server.phwang_modules.util_modules.list_mgr

    def importLogit(self):
        return go_server.phwang_modules.util_modules.logit

    def mallocQueue(self):
        return require("../util_modules/queue.js").malloc(self.rootObject());

    def mallocRing(self):
        return require("../util_modules/ring.js").malloc(self.rootObject());
