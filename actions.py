import numpy as mp
import random as rd

# R = [1,2,-1], Ri = [1,2,1]
# L = [1,0,1] , Li = [1,0,-1]
# U = [0,0,-1], Ui = [0,0,1]
# D = [0,2,1] , Di = [0,2,1]
# F = [2,2,1] , Fi = [2,2,-1]
# B = [2,0,1] , Bi = [2,0,-1]



class Actions():
    
    DICO = {'R':[1,2,-1] , 'Ri':[1,2, 1], 
            'L':[1,0, 1] , 'Li':[1,0,-1], 
            'U':[0,0,-1] , 'Ui':[0,0, 1], 
            'D':[0,2, 1] , 'Di':[0,2,-1], 
            'F':[2,2, 1] , 'Fi':[2,2,-1], 
            'B':[2,0, 1] , 'Bi':[2,0,-1]}
    ACTIONS = [*DICO]
    
    
    def __init__(self, cube):
        self.cube = cube
        
    def makeOneAction(self, action):
        # In eache side, ther are 3 blocks of 3 tile
        # action(number of block (0...DIM-1) ; angle of move (-1,1) )
        # there are 3 of concatenate sides: 
        # func0 ==> List0 = left, front, right, back
        # func1 ==> List1 = left, bottom, right, Top
        # func2 ==> List2 = top, front, bottom, back
        
        func, subAction = Actions.DICO[action][0], (Actions.DICO[action][1], Actions.DICO[action][2])
        
        if func == 0:
            self.wrapper(self.cube.changeList0, subAction)
        elif func == 1:
            self.wrapper(self.cube.changeList1, subAction)
        else:
            self.wrapper(self.cube.changeList2, subAction)
               
        return self.cube.master, self.cube.masterAsInt
        
        
    def makeRandomActions(self, last_1):
        action = rd.choice(Actions.ACTIONS)
        action_i = self.getOpposite(action)

        while last_1 == action_i:
            action = rd.choice(Actions.ACTIONS)
            action_i = self.getOpposite(action)

        self.cube.master, self.cube.masterAsInt = self.makeOneAction(action)
        
        last_1 = action
        
        return last_1, action, action_i, self.cube.master, self.cube.masterAsInt
        
        
    def wrapper(self, func, *args): 
        func(*args)

        
    def getOpposite(self, action): 
        if len(action) == 2:
            return action[0]
        else:
            return action + 'i'
    
    def sameSide(self, x): 
        return  x.count(x[0]) == len(x)
       