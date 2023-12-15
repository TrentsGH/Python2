from tkinter import *
import numpy as np
import math
#
WireResistivityByType = {'copper':1.0}

class port:
    def __init__(self,master,x,y,symbol = ''):
        self.x = x
        self.y = y
        self.type = 'port'
        self.master = master
        self.circle = self.master.create_oval(x-8,y-8,x+8,y+8,fill='grey',activefill='green')
        self.text = self.master.create_text(x,y,text=symbol,anchor=CENTER,font=('times new roman bold',16))
    def Move(self,x,y):
        self.master.coords(self.circle,x-8,y-8,x+8,y+8)
        self.master.coords(self.text,x,y)
        self.x = x
        self.y = y
        
        

    
class dc_battery:
    def __init__(self,master,x1,y1, voltage = 1.0):
        self.master = master.board
        self.root = master
        self.type = 'dc battery'
        self.id = self.master.create_rectangle(x1-25,y1-50,x1+25,y1+50,fill='',activefill='white')
        self.positive = port(self.master,x1-25,y1-50,symbol='+')
        self.x1 = x1
        self.y1 = y1
        
        master.addObject(self)
        
        self.master.tag_bind(self.id,'<B1-Motion>',self.Move)
        '''
        self.master.tag_bind(self.id,'<Double-Button-1>',self.Rotate)
        self.master.tag_bind(self.id,'<Enter>',self.info)'''
    def Move(self,event):
        self.master.coords(self.id,-25+event.x,-50+event.y,25+event.x,50+event.y)
        self.positive.Move(-25+event.x,-50+event.y) 
        self.x1 = event.x
        self.y1 = event.y
        
class wireSeg:
    def __init__(self,master,x1,y1,x2,y2,material='copper',guage=1.0):
        self.master = master.board
        self.root = master
        self.type = 'wire' 
        self.id = self.master.create_line(x1,y1,x2,y2,fill='black',width=int(guage*5),activefill='white')
        
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.XL = abs(x1-x2)
        self.YL = abs(y1-y2)
        self.angle = np.degrees(np.arctan(float(y1-y2)/float(x2-x1)))
        self.crossArea = guage
        self.material = material
        master.addObject(self)
        self.master.tag_bind(self.id,'<B1-Motion>',self.Move)
        self.master.tag_bind(self.id,'<Double-Button-1>',self.Rotate)
        self.master.tag_bind(self.id,'<Enter>',self.info)
        
    def Move(self,event):
        self.master.coords(self.id,-self.XL/2+event.x,-self.YL/2+event.y,self.XL/2+event.x,self.YL/2+event.y)
        self.x1 = -self.XL/2+event.x
        self.x2 = self.XL/2+event.x
        self.y1 = -self.YL/2+event.y
        self.y2 = self.YL/2+event.y
        print(self.angle)

    def info(self,event):
        print('Resistance: ',self.getRes())
        
    def Rotate(self,event):
        cx = (self.x2+self.x1)/2
        cy = (self.y2+self.y1)/2
        r = 0.5*np.sqrt((self.x2-self.x1)**(2)+(self.y2-self.y1)**(2))
        
        self.master.coords(self.id,self.x1,self.y1,self.x2,self.y2)
    def getRes(self):
        r = WireResistivityByType[self.material]
        L = np.sqrt(((self.x2-self.x1)*self.getScale('x'))**(2)+
                    ((self.y2-self.y1)*self.getScale('y'))**(2))
        res = r*L/self.crossArea
        return res

    def getScale(self,direction):
        if direction == 'x':
            cm = self.root.sizex
            masterSize = self.master.winfo_width()-4
            return float(cm)/float(masterSize)
        if direction == 'y':
            cm = self.root.sizey
            masterSize = self.master.winfo_height()-4
            return float(cm)/float(masterSize)
        
    def delt(self,x=None):
        self.master.delete(self.id)
        root.objects.remove(self)
        root.types[self.type].remove(self.id)
        del(self)
        
        

class circuitBoard:
    def __init__(self,master,sizex = 5, sizey =3,width=600,height=400):
        self.master = master
        self.board = Canvas(root,bg='light green',width=width,height = height)
        self.board.pack(expand=True,fill = BOTH)
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
    def buildGrid(self):
        for i in range(16):
            dx = self.width/16
            self.grid.append(self.board.create_line((i+1)*dx,0,(i+1)*dx,500,fill='grey'))
        for i in range(16):
            dy = self.height/16
            self.grid.append(self.board.create_line(0,(i+1)*dy,800,(i+1)*dy,fill='grey'))
        self.board.create_oval((self.width/2)-2,(self.height/2)-2,(self.width/2)+2,(self.height/2)+2,fill='red')
        
    def addObject(self,x):
        self.objects.append(x)
        self.types[x.type].append(self.objects.index(x))
        
root = Tk()
menuFrame = Frame(root,width=125)
menuFrame.pack(fill=Y,side=LEFT)
Label(menuFrame,text='Add Circuit Object',font=('times new roman bold',15),width=20,bg='dark grey').pack()
CB = circuitBoard(root)
wireSeg(CB,0,25,100,100)
dc_battery(CB,100,100)
mainloop()
