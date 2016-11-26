def malloc(root_object_val):
    return ClusterBaseClass(root_object_val)

class ClusterBaseClass(object):
    def __init__(self, root_object_val):
        self.theRootObject = root_object_val
        self.theGlobalClusterId = 100
        self.theClusterQueue = self.rootObject().importObject().mallocQueue()
        self.debug(True, "init__", "")

    def clusterModuleMalloc(self, topic_data_val, session_val):
        return self.rootObject().importObject().importCluster().malloc(self.rootObject(), topic_data_val, session_val)

    def objectName(self):
        return "ClusterBaseClass"

    def rootObject(self):
        return self.theRootObject

    def utilObject(self):
        return self.rootObject().utilObject()

    def globalClusterId(self):
        return self.theGlobalClusterId

    def incrementGlobalClusterId(self):
        self.theGlobalClusterId += 1

    def mallocCluster(self, topic_val, cluster_val):
        entry = self.clusterModuleMalloc(topic_val, cluster_val)
        self.incrementGlobalClusterId()
        return entry

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
