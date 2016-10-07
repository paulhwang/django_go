def malloc(fibre_val):
    return LinkMgrClass(fibre_val)

class LinkMgrClass(object):
    def __init__(self, fibre_val):
        self.theFibreObject = fibre_val;
