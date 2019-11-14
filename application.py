import random as rd
import numpy as np
import collections
import time, sys

from affichage import Affichage
from createcube import Cube
from actions import Actions


class App():
    def __init__(self,dim):
                
        # display a view of the cube in canvas
        self.dim = dim
        self.affichage = Affichage(self.dim)
        self.restApp()
        
        
    def restApp(self):
        # create a cube with dimension, view and colors 
        self.createCube()
        # create agent
        self.createAgent()
        
    def createCube(self):
        # create a cube with dimension, view and colors 
        self.myCube = Cube(self.dim) # create the cube
        self.myView = self.myCube.view
        self.myMaster = self.myCube.master # get the master view
        self.myMasterAsInt = self.myCube.masterAsInt # get the master view
        
            
    def createAgent(self):
        # create agent
        self.agent = Actions(self.myCube)
        self.actions = []
        self.reversedOppositeActions = []
            
        
    def oneActionState(self, action):
        self.myMaster, self.myMasterAsInt = self.agent.makeOneAction(action)
        

    def manyActionsState(self, nb_time): 
        last_1 = "A"
        temp = []
        for _ in range(nb_time):  
            last_1, action, action_i, self.myMaster, self.myMasterAsInt = self.agent.makeRandomActions(last_1)
            self.actions.append(action)
            temp.append(action_i)
        
        temp.reverse()
        self.reversedOppositeActions = temp
        del temp
        
    
        
    def updateWindow(self):
        self.affichage.showCube(self.myMaster, self.myView)
        self.affichage.window.update_idletasks()
        self.affichage.window.update()
        time.sleep(0.05)
        
        
    def quit(self, temps=0.0):
        self.affichage.quit(temps)
        
    def num_solved_sides(self): # compte le nombre de face résolue
        solved = 0
        for side in self.myMaster:
            color = side[0][0]
            # if number of pieces on this side equal to first square is number of total pieces, side is solved
            if sum(collections.Counter(row)[color] for row in side) == self.dim**2:
                solved += 1

        return solved  