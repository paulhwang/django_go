import go_server.project_modules.fibre_modules.cluster

def malloc(fibre_val):
    return ClusterMgrClass(fibre_val)

def malloc_cluster(cluster_mgr_val):
    return go_server.project_modules.fibre_modules.cluster.malloc(cluster_mgr_val)

class ClusterMgrClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val;
        self.theClusterObject = malloc_cluster(self)

    def className(self):
        return "ClusterMgrClass"

    def fibreObject(self):
        return self.theFibreObject