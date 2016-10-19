import go_server.phwang_modules.farbric_modules.cluster

def malloc(fabric_val):
    return ClusterMgrClass(fabric_val)

def malloc_cluster(cluster_mgr_val):
    return go_server.phwang_modules.farbric_modules.cluster.malloc(cluster_mgr_val)

class ClusterMgrClass(object):
    def __init__(self, fabric_val):
        self.theFarbricObject = fabric_val;
        self.theClusterObject = malloc_cluster(self)

    def mallocCluster(self):
        return malloc_cluster(self)

    def className(self):
        return "ClusterMgrClass"

    def farbricObject(self):
        return self.theFarbricObject

    def phwangObject(self):
        return self.farbricObject().phwangObject()

    def utilObject(self):
        return self.phwangObject().utilObject()

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.farbricObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.farbricObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
