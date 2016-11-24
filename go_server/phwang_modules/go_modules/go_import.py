import go_server.phwang_modules.util_modules.logit
import go_server.phwang_modules.util_modules.list_mgr
import go_server.phwang_modules.util_modules.queue
import go_server.phwang_modules.util_modules.ring
import go_server.phwang_modules.go_modules.go_base
import go_server.phwang_modules.go_modules.go_config
import go_server.phwang_modules.go_modules.go_board
import go_server.phwang_modules.go_modules.go_engine
import go_server.phwang_modules.go_modules.go_game
import go_server.phwang_modules.go_modules.go_port
import go_server.phwang_modules.go_modules.go_move
import go_server.phwang_modules.go_modules.go_group_list
import go_server.phwang_modules.go_modules.go_group

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
        return go_server.phwang_modules.go_modules.go_config

    def importMove(self):
        return go_server.phwang_modules.go_modules.go_move

    def importBoard(self):
        return go_server.phwang_modules.go_modules.go_board

    def importGame(self):
        return go_server.phwang_modules.go_modules.go_game

    def importPort(self):
        return go_server.phwang_modules.go_modules.go_port

    def importEngine(self):
        return go_server.phwang_modules.go_modules.go_engine

    def importGroup(self):
        return go_server.phwang_modules.go_modules.go_group

    def importGroupList(self):
        return go_server.phwang_modules.go_modules.go_group_list

    def importListMgr(self):
        return go_server.phwang_modules.util_modules.list_mgr

    def importLogit(self):
        return go_server.phwang_modules.util_modules.logit

    def mallocQueue(self):
        return go_server.phwang_modules.util_modules.queue.malloc(self.rootObject())

    def mallocRing(self):
        return go_server.phwang_modules.util_modules.ring.malloc(self.rootObject())
