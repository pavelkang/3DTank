# This module is a collection of helper functions
def clampAngle(self, angle):
    while angle < -180:
        angle += 360
    while angle >180:
        angle -= 360
    return angle

