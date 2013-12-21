# This is a 3D NES Tank game

from panda3d.core import loadPrcFileData
configVars = """
show-frame-rate-meter #t
"""
loadPrcFileData('', configVars)

from direct.showbase.ShowBase import ShowBase
from load import *
from panda3d.core import *
import sys
from control import keyControl
from lighting import *
from preload import *

TANK_SPEED = 5

class tankWorld(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.adjustCamera()
        loadEverything(self)
        addLight(self)
        keyControl(self)
        base.disableMouse()
        self.initVars()

    def initVars(self):
        self.headingDir = None

    def moveTank(self, direction):
        if direction == 'u':
            self.tank.setY(self.tank.getY()+TANK_SPEED)
            if self.headingDir != 'u':
                self.tank.setH(180)
        elif direction == 'd':
            self.tank.setY(self.tank.getY()-TANK_SPEED)
            if self.headingDir != 'd':
                self.tank.setH(0)
        elif direction == 'l':
            self.tank.setX(self.tank.getX()-TANK_SPEED)
            if self.headingDir != 'l':
                self.tank.setH(270)
        else:
            self.tank.setX(self.tank.getX()+TANK_SPEED)
            if self.headingDir != 'r':
                self.tank.setH(90)

    def adjustCamera(self):
        self.camera.setPos(0, 0, 2600)
        self.camera.setHpr(0, -90, 0)

if __name__ == "__main__":
    game = tankWorld()
    game.run()
    
