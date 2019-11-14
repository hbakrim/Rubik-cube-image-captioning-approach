#import time, sys

from tkinter import *
from tkinter.font import Font
import numpy as np
import time


class Affichage():
    

    def __init__(self, dim):
        self.window = Tk()
        self.canvas = Canvas(self.window, bg = "gray", height = 500, width = 620)
        self.canvas.pack()
        self.dim = dim
        

    ###########################################################
    def showCube(self, master, view): 
        
        
        FONT = Font(family="Helvetica", size=10)
        MARGE = 10
        DELTA = 50
        def point(n):
            return (MARGE + DELTA * n, MARGE + DELTA * (n+1))
        
        for i, param in enumerate([[1,0],[0,1],[1,1],[2,1],[3,1],[1,2]]):
            colorList = np.concatenate(master[i], axis=0).tolist()
            param = [x * self.dim for x in param]
            posi = {'x':point(param[0]), 'y':point(param[1])}
            self._createRectangle(posi, colorList)
        
        for i, point in enumerate([[233, 83], [90, 230], [233, 230], [390, 230], [540, 230], [233, 380]]):
            self.canvas.create_text((point[0], point[1]), text=view[i][0].upper(), font=FONT, fill='black')
        

        
    ###########################################################
    def _createRectangle(self, posi, colorList):
        colors_dico = {'w':'white', 'b':'blue', "r":'red', 'g':'green', 'o':'orange', 'y':'yellow'}
        k = 0
        for j in range(self.dim):
            for i in range(self.dim):
                self.canvas.create_rectangle(posi['x'][0]+50*i,
                                             posi['y'][0]+50*j,
                                             posi['x'][1]+50*i,
                                             posi['y'][1]+50*j,width=2,fill=colors_dico[colorList[k][0]])
                k += 1

    ###################################################
    def quit(self, temps):
        time.sleep(temps)
        self.window.destroy()
     