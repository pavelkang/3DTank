# This module helps load resources
from direct.showbase.ShowBase import ShowBase
import os

def load_model(name):
    filePath = os.path.join('..','data','models',name)
    try:
        file = loader.loadModel(filePath)
    except:
        raise SystemExit, "Failed to import model %s" %name
    return file

def load_tex(name):
    filePath = os.path.join('..','data','textures',name)
    try:
        file = loader.loadTexture(filePath)
    except:
        raise SystemExit, "Failed to import texture %s" %name
    return file
