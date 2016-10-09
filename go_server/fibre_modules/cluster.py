def malloc(cluster_mgr_val):
    return ClusterClass(cluster_mgr_val)

class ClusterClass(object):
    def __init__(self, cluster_mgr_val):
        self.theClusterMgrObject = cluster_mgr_val;

    def className(self):
        return "ClusterClass"

    def clusterMgrObject(self):
        return self.theClusterMgrObject
