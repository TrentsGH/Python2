from tkinter import *
import numpy as np
import math
from tkColorFunction import rgb, numColor
import PIL

def mainBuild(event):
    if mode.get() == 1:
        print('Create Mode')
        battery(board,event.x,event.y,10)
    elif mode.get() ==2:
        print('Connect Mode')
class obj:
    def __init__(self,master,Type):
        self.master = master
        self.gui = master.gui
        self.type = Type
        self.ids = []
        self.UID = None
        self.ports = {} # {port#: [value,x,y]}
        self.links = {} # {obj: [port#1,port#2]}
        self.lines = {}
        

    def link(self,port1,port2,x,first=True):
        self.links[x]=[port1,port2]
        if first:
            x.link(port2,port1,self,False)
            self.drawLinks()
            
            
    def getPortValue(self,x):
        return self.ports[x][0]

    def moveID(self,id,x,y,dx=None,dy=None):
        try:
            self.gui.coords(id,x-dx,y-dy,x+dx,y+dy)
        except:
            self.gui.coords(id,x,y)
            
    def bindAll(self,action,function):
        for i in self.ids:
            self.gui.tag_bind(i,action,function)
            
    def uniqueID(self):
        self.UID = hash(str(self.ids))

    def drawLinks(self):
        for i in self.links:
            pair = self.links[i]
            x1 = self.ports[pair[0]][1]
            y1 = self.ports[pair[0]][2]
            x2 = i.ports[pair[1]][1]
            y2 = i.ports[pair[1]][2]
        self.lines[i] = self.gui.create_line(x1,y1,x2,y2)
        i.lines[self] = self.gui.create_line(x1,y1,x2,y2)

    def reDrawLinks(self):
        for i in self.links:
            pair = self.links[i]
            x1 = self.ports[pair[0]][1]
            y1 = self.ports[pair[0]][2]
            x2 = i.ports[pair[1]][1]
            y2 = i.ports[pair[1]][2]
            self.gui.coords(self.lines[i],x1,y1,x2,y2)
            self.gui.coords(i.lines[self],x1,y1,x2,y2)

            

    
    
        
        
            
            

    
        

    

class battery(obj):
    def __init__(self,master,x,y,volts):
        super().__init__(master,'dc battery')
        
        self.dx = 15
        self.dy = 25
        self.pdx = 4
        self.pdy = 4
        self.p1x = x-self.dx+self.pdx
        self.p1y = y-self.dy-self.pdy
        self.p2x = x+self.dx-self.pdx
        self.p2y = y-self.dy-self.pdy
        self.ports[1] = [volts,self.p1x,self.p1y]
        self.ports[2] = [0,self.p2x,self.p2y]
        self.x = x
        self.y = y
        #creates rectangle body
        self.ids.append(self.gui.create_rectangle(self.x-self.dx,self.y-self.dy,
                                                  self.x+self.dx,self.y+self.dy,fill='white'))
        self.ids.append(self.gui.create_rectangle(self.p1x-self.pdx,self.p1y-self.pdy,
                                                  self.p1x+self.pdx,self.p1y+self.pdy,fill='white'))
        self.ids.append(self.gui.create_text(self.p1x,self.p1y,text='+'))
        self.ids.append(self.gui.create_rectangle(self.p2x-self.pdx,self.p2y-self.pdy,
                                                  self.p2x+self.pdx,self.p2y+self.pdy,fill='white'))
        self.ids.append(self.gui.create_text(self.p2x,self.p2y,text='-'))
        self.uniqueID()
        self.bindAll('<B1-Motion>',self.move)
    def move(self,event):
        self.x = event.x
        self.y = event.y
        self.moveID(self.ids[0],event.x,event.y,self.dx,self.dy)
        self.genPos()
        self.moveID(self.ids[1],self.p1x,self.p1y,self.pdx,self.pdy)
        self.moveID(self.ids[2],self.p1x,self.p1y,self.pdx,self.pdy)
        self.moveID(self.ids[3],self.p2x,self.p2y,self.pdx,self.pdy)
        self.moveID(self.ids[4],self.p2x,self.p2y,self.pdx,self.pdy)
        self.reDrawLinks()

    def genPos(self):
        self.p1x = self.x-self.dx+self.pdx
        self.p1y = self.y-self.dy-self.pdy
        self.ports[1] = [self.ports[1][0]]+[self.p1x,self.p1y]
        self.p2x = self.x+self.dx-self.pdx
        self.p2y = self.y-self.dy-self.pdy
        self.ports[2] = [self.ports[2][0]]+[self.p2x,self.p2y]
        

    


class LiveGUI:
    def __init__(self,master,bg='',sizex = 5, sizey =3,width=600,height=400,side=RIGHT):
        self.master = master
        self.gui = Canvas(root,bg='light green',width=width,height = height)
        self.gui.pack(expand=True,fill = BOTH,side=side)
        self.sizex = sizex
        self.sizey = sizey
        self.grid = []
        self.width = width
        self.height = height
        self.buildGrid()
        self.objects = []
        self.connections = []
        self.types = {'wire':[],
                      'dc battery':[],
                      'resistor':[],
                      'ac battery':[],
                      'inductor':[],
                      'capacitor':[]
                      }
        self.connect = False
        self.gui.bind('<Double-Button-1>',mainBuild)
    def buildGrid(self):
        for i in range(16):
            dx = self.width/16
            self.grid.append(self.gui.create_line((i+1)*dx,0,(i+1)*dx,500,fill='grey'))
        for i in range(16):
            dy = self.height/16
            self.grid.append(self.gui.create_line(0,(i+1)*dy,800,(i+1)*dy,fill='grey'))
        self.gui.create_oval((self.width/2)-2,(self.height/2)-2,(self.width/2)+2,(self.height/2)+2,fill='red')
        
    def addObject(self,x):
        self.objects.append(x)
        self.types[x.type].append(self.objects.index(x))

    

    

root = Tk()
board = LiveGUI(root)
menuFrame = Frame(root)
menuFrame.pack(side=LEFT)
Label(menuFrame,text='Control Panel',anchor='n',
      font=('Times New Roman bold',15),bg='grey',width=20).pack()

modeFrame = Frame(menuFrame)
modeFrame.pack()

mode = IntVar()
values = {'Creation Mode':1,
          'Connection Mode':2}
for i in values:
    Radiobutton(modeFrame,variable = mode,value = values[i],text=i,anchor='e').pack()


mainloop()
