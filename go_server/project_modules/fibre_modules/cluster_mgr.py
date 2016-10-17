import go_server.project_modules.fibre_modules.cluster

def malloc(fibre_val):
    return ClusterMgrClass(fibre_val)

def malloc_cluster(cluster_mgr_val):
    return go_server.project_modules.fibre_modules.cluster.malloc(cluster_mgr_val)

class ClusterMgrClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val;
        self.theClusterObject = malloc_cluster(self)

    def mallocCluster(self):
        return malloc_cluster(self)

    def className(self):
        return "ClusterMgrClass"

    def fibreObject(self):
        return self.theFibreObject

    def rootObject(self):
        return self.fibreObject().rootObject()

    def utilObject(self):
        return self.rootObject().utilObject()

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().logit(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.fibreObject().abend(self.className() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
