# this module deals with keyboard input
import sys

def keyControl(self):
    self.accept('escape', sys.exit)
    self.accept("w-repeat",self.moveTank,["u"])
    self.accept("s-repeat",self.moveTank,["d"])
    self.accept("a-repeat",self.moveTank,["l"])
    self.accept("d-repeat",self.moveTank,["r"])

    
