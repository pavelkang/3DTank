# This module deals with lighting in the game
from panda3d.core import *

def addDirLight(self):
    dirLight = DirectionalLight("directional")
    dirLight.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
    dirNode = self.render.attachNewNode(dirLight)
    dirNode.setHpr(60, 0, -90)
    render.setLight(dirNode)

def addAmbientLight(self):
    ambLight = AmbientLight("ambient")
    ambLight.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
    ambNode = self.render.attachNewNode(ambLight)
    render.setLight(ambNode)

def addLight(self):
    addDirLight(self)
    addAmbientLight(self)
    
