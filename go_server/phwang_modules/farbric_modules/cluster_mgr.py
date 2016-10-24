import go_server.phwang_modules.farbric_modules.cluster

def malloc(fabric_val):
    return ClusterMgrClass(fabric_val)

def malloc_cluster(cluster_mgr_val, topic_val, session_val):
    return go_server.phwang_modules.farbric_modules.cluster.malloc(cluster_mgr_val, topic_val, session_val)

class ClusterMgrClass(object):
    def __init__(self, fabric_val):
        self.theFarbricObject = fabric_val
        self.theGlobalClusterId = 100
        self.theClusterQueue = self.utilObject().mallocQueue()

    def clusterModuleMalloc(self, topic_val, session_val):
        return malloc_cluster(self, topic_val, session_val)

    def className(self):
        return "ClusterMgrClass"

    def farbricObject(self):
        return self.theFarbricObject

    def phwangObject(self):
        return self.farbricObject().phwangObject()

    def utilObject(self):
        return self.phwangObject().utilObject()

    def globalClusterId(self):
        return self.theGlobalClusterId

    def incrementGlobalClusterId(self):
        self.theGlobalClusterId += 1

    def mallocCluster(self, topic_val, session_val):
        entry = self.clusterModuleMalloc(topic_val, session_val)
        self.incrementGlobalClusterId()
        return entry

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.farbricObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.farbricObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
