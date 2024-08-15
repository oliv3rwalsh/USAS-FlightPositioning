import math

class Point:
    def __init__(self, xpos=0, ypos=0, zpos=0):
        self.x = xpos
        self.y = ypos
        self.z = zpos
    def updatepoint(self, xpos, ypos, zpos):
        self.x = xpos
        self.y = ypos
        self.z = zpos
    def adjustpoint(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz
    def distancefrom(self, point):
        deltax = self.x - point.x
        deltay = self.y - point.y
        deltaz = self.z - point.z
        temp = deltax ** 2 + deltay ** 2 + deltaz ** 2
        return round(math.sqrt(temp), 2)