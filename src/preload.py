# This module preloads the models in the scene
from load import *

START_POS = (0, 0, -20)

Y_UP = 600
Y_DOWN = -600
X_LEFT = -600
X_RIGHT = 600

def loadTank(self):
    self.tank = load_model("tank.egg")
    self.tank.reparentTo(render)
    self.tank.setPos(START_POS)
    # bug here
    self.tank_tex = load_tex("camouflage.jpg")
    self.tank.setTexture(self.tank_tex)

def loadEnviron(self):
    self.environ = load_model("world_tank_world.egg")
    self.environ.reparentTo(render)
    self.environ.setPos(-700,0,0)
    self.environ.setHpr(0,0,0)    

def loadEverything(self):
    loadTank(self)
    loadEnviron(self)
