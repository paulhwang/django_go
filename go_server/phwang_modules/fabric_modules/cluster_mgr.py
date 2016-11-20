import go_server.phwang_modules.fabric_modules.cluster

def malloc(fabric_object_val):
    return ClusterMgrClass(fabric_object_val)

def malloc_cluster(cluster_mgr_val, topic_data_val, session_val):
    return go_server.phwang_modules.fabric_modules.cluster.malloc(cluster_mgr_val, topic_data_val, session_val)

class ClusterMgrClass(object):
    def __init__(self, fabric_object_val):
        self.theFarbricObject = fabric_object_val
        self.theGlobalClusterId = 100
        self.theClusterQueue = self.utilObject().mallocQueue()
        self.debug(True, "init__", "")

    def clusterModuleMalloc(self, topic_data_val, session_val):
        return malloc_cluster(self, topic_data_val, session_val)

    def objectName(self):
        return "ClusterMgrClass"

    def fabricObject(self):
        return self.theFarbricObject

    def rootObject(self):
        return self.fabricObject().rootObject()

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

    def insertSessionToList(self, cluster_val):
        if not cluster_val:
            self.abend("enQueue", "null cluster_val")
            return

        self.abendIt()

        self.incrementSize()
        if not self.head():
            cluster_val.setPrev(None)
            cluster_val.setNext(None)
            self.setHead(cluster_val)
            self.setTail(cluster_val)
        else:
            self.tail().setNext(cluster_val)
            cluster_val.setPrev(self.tail())
            cluster_val.setNext(None)
            self.setTail(cluster_val)
        self.abendIt()

    def deleteSessionFromList(self, cluster_val):
        if self.size() <= 0:
            self.abend("deleteSessionFromList", "size=%i", self.size())
            return
        if not self.clusterExistInTheList(cluster_val):
            self.abend("deleteSessionFromList", "sessionExistInTheList is false")
            return

        self.abendIt()
        if cluster_val.prev():
            cluster_val.prev().setNext(cluster_val.next())
        else:
            self.setHead(cluster_val.next())
        if cluster_val.next():
            cluster_val.next().setPrev(cluster_val.prev())
        else:
            self.setTail(cluster_val.prev())
        self.decrementSize()
        self.abendIt()

    def clusterExistInTheList(self, cluster_val):
        cluster = self.head()
        while cluster:
            if cluster == cluster_val:
                return True
            cluster = cluster.next()
        return False

    def abendIt(self):
        i = 0;
        cluster = self.head()
        while cluster:
            cluster = cluster.next()
            i += 1
        if i != self.size():
            self.abend("abendIt", "head: size=%i i=%i", self.size(), i)

        i = 0
        cluster = self.tail()
        while cluster:
            cluster = cluster.prev()
            i += 1
        if i != self.size():
            self.abend("abendIt", "tail: size=%i i=%i", self.size(), i)

    def debug(self, bool_val, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        if bool_val:
            self.logit(str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def logit(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().LOG_IT(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)

    def abend(self, str1, str2, str3 = "", str4 = "", str5 = "", str6 = "", str7 = "", str8 = "", str9 = "", str10 = "", str11 = ""):
        self.rootObject().ABEND(self.objectName() + "." + str1 + "() ", str2, str3, str4, str5, str6, str7, str8, str9, str10, str11)
