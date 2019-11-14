import numpy as np
import itertools


class Cube():
    COLORS = ['w', 'b', 'r', 'g', 'o', 'y']
    INT_COLOR = {i:color for i, color in enumerate(COLORS)}
    COLOR_INT = {value:key for key, value in INT_COLOR.items()}
    VIEW = ['U', 'L', 'F', 'R', 'B', 'D']
    def __init__(self, dim):
        
        self.dim = dim
        self.view = Cube.VIEW
        #self.colors = colors
        # Define eache side with color: {name of side: color}
        self.sideDic = {side: self.createSide(couleur) for side, couleur in zip(self.view, Cube.COLORS)}
        #Choose a master view: what is order top => left => front => right => back => bottom, sides
        self.master = np.array([self.sideDic[side].tolist() for side in self.view])
        self.masterAsInt = self.cube2int()
        
        
    def createSide(self, couleur):
        return np.array([couleur]*self.dim*self.dim).reshape((self.dim,self.dim))
    
    
    def cube2int(self):
        return np.vectorize(Cube.COLOR_INT.get)(self.master)
    
    
    def int2cube(self):
        return np.vectorize(Cube.INT_COLOR.get)(self.masterAsInt) 
    
    
    def setMaster(self, master):
        self.master = master
        self.masterAsInt = self.cube2int()
        
    def setMasterAsInt(self, masterAsInt):
        self.masterAsInt = masterAsInt
        self.master = self.int2cube()
      
    
    def changeList0(self, subAction):
        # List1 = left, front, right, back
        # the action in the list1 is in rows
        master = self.master.copy()
        (row, step) = subAction
        conca = np.concatenate((master[1:-1]), axis=1)
        conca[row] = np.roll(conca[row], step*self.dim)
        if row == 0:
            lst = [np.rot90(master[0], step)] + np.hsplit(conca, 4) + [master[-1]]
        elif row == self.dim-1:
            lst = [master[0]] + np.hsplit(conca, 4) + [np.rot90(master[-1], -step)]
        elif self.dim > 2:
            lst = [master[0]] + np.hsplit(conca, 4) + [master[-1]]
        self.master = np.concatenate(lst, axis=0).reshape((6,self.dim,self.dim))
        self.masterAsInt = self.cube2int()
        del master, lst, conca
        

    
    def changeList1(self, subAction):
        # List2 = left, bottom, right, Top
        # the action in the list2 is in columns
        master = self.master.copy()
        (column, step) = subAction
        conca = np.vstack((master[0],master[2],master[5],np.flipud(np.fliplr(master[4]))))
        conca = np.hsplit(conca, self.dim)
        conca[column] = np.roll(np.hstack(conca[column]), step*self.dim).reshape((-1,1))
        conca = np.hstack(conca).reshape((4,self.dim,self.dim))
        a = np.flipud(np.fliplr(conca[3]))
        if column == 0:
            lst = (conca[0], np.rot90(master[1],-step), conca[1], master[3], a, conca[2])
        elif column == self.dim-1:
            lst = (conca[0], master[1], conca[1], np.rot90(master[3],step), a, conca[2]) 
        elif self.dim > 2:
            lst = (conca[0], master[1], conca[1], master[3], a, conca[2])
        self.master = np.concatenate(lst, axis=0).reshape((6,self.dim,self.dim))
        self.masterAsInt = self.cube2int()
        del master, lst, conca
            
                
    def changeList2(self, subAction):
        # List3 = top, front, bottom, back
        # the action in the list3 is in row and column
        master = self.master.copy()
        (row_column, step) = subAction
        conca = np.hstack((master[0],np.rot90(master[3]),np.rot90(master[5],2),np.rot90(master[1],3)))
        conca[row_column] = np.roll(conca[row_column], step*self.dim)
        lst0 = np.hsplit(conca, 4)
        if row_column == 0:
            lst = [lst0[0]] + [np.rot90(lst0[3], 1)] + [master[2]] + [np.rot90(lst0[1], -1)] + [np.fliplr(np.rot90(np.fliplr(master[4]),-step))] + [np.rot90(lst0[2], -2)]
        elif row_column == self.dim-1:
            lst = [lst0[0]] + [np.rot90(lst0[3], 1)] + [np.rot90(master[2],-step)] + [np.rot90(lst0[1], -1)] + [master[4]] + [np.rot90(lst0[2], -2)]
        elif self.dim > 2:
            lst = [lst0[0]] + [np.rot90(lst0[3], 1)] + [master[2]] + [np.rot90(lst0[1], -1)] + [master[4]] + [np.rot90(lst0[2], -2)]
        self.master = np.concatenate(lst, axis=0).reshape((6,self.dim,self.dim))
        self.masterAsInt = self.cube2int()
        del master, lst, lst0, conca 
   