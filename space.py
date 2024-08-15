class Space():
    def __init__(self, centerpoint, radius):
        self.x = centerpoint.x
        self.y = centerpoint.y
        self.z = centerpoint.z
        self.p = centerpoint
        self.r = radius
    def contains(self, point):
        if point.distancefrom(self.p) <= self.r:
            return True
        return False