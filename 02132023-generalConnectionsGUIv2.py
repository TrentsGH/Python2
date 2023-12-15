from tkinter import *


class port:
    def __init__(self,master,value,x,y,type=None,relation = None,label='Port',bind = None,units='volts'):
        self.master = master
        self.gui = master.gui
        self.value = value
        self.connections = []
        self.x = x
        self.y = y
        self.dx = 5
        self.dy = 5
        self.visual = self.gui.create_oval(self.x-self.dx,self.y-self.dy,self.x+self.dx,self.y+self.dy,fill='light green',activefill='blue',outline='')
        #self.gui.tag_bind(self.visual,'<B1-Motion>',self.cMove)
        self.gui.tag_bind(self.visual,'<Enter>',self.showInfo)
        self.gui.tag_bind(self.visual,'<Leave>',self.master.hideInfo)
        self.gui.tag_bind(self.visual,'<Double-Button-1>',self.StartConnect)
        self.relation=relation
        self.id = label
        self.bind = bind
        self.units = units
        self.gui.tag_bind(self.visual,'<B1-Motion>',self.bind.move)
        

    def StartConnect(self,exent):
        if self.master.connect == None:
            self.master.connect = self
            self.gui.itemconfig(self.visual,fill='blue')
        else:
            self.connect(self.master.connect)
            self.gui.itemconfig(self.master.connect.visual,fill='light green')
            self.gui.itemconfig(self.visual,fill='light green')
            self.master.connect = None
            
        
    def connect(self,port2):
        line = self.gui.create_line(self.x,self.y,port2.x,port2.y,dash=(1,5),width=2,activefill='white')
        self.gui.tag_bind(line,'<Double-Button-3>',lambda event,a=port2,b=line:self.disConnect(a,b))
        self.gui.tag_raise(self.visual,line)
        self.gui.tag_raise(port2.visual,line)
        self.gui.tag_raise(port2.visual,line)
        self.connections.append([port2,line])
        port2.connections.append([self,line])

    def disConnect(self,port2,line):
        self.connections.remove([port2,line])
        port2.connections.remove([self,line])
        self.gui.delete(line)
        
        
    def cMove(self,event):
        self.move(event.x,event.y)
        
    def move(self,x,y):
        self.x = x
        self.y = y
        self.gui.coords(self.visual,self.x-self.dx,self.y-self.dy,self.x+self.dx,self.y+self.dy)
        for i in range(len(self.connections)):
            port2 = self.connections[i][0]
            line = self.connections[i][1]
            self.gui.coords(line,self.x,self.y,port2.x,port2.y)
            

    def update(self,value):
        self.value = value

    def showInfo(self,event):
        cons = ''
        for i in self.connections:
            cons+=str(i[0].visual)+', '
        text = '''Port Label: {0}
Port ID   : {1}
Port Rel  : {2}
Port Value: {3} {4}
Connections: {5}'''.format(self.id,self.visual,self.relation,self.value,self.units,cons)
        self.master.showInfo(event,text)

class obj:
    def __init__(self,master,x,y,v1,v2,type = 'dc battery',orientation = 'v',units='volts'):
        self.master = master
        self.gui = master.gui
        self.x = x
        self.y = y
        self.d = 8
        if orientation == 'v':
            self.dx = 0
            self.dy = 5
        else:
            self.dx = 5
            self.dy = 0
        self.p1 = port(master,v1,x-self.dx,y-self.dy,relation=type,label = 'Front Port',bind=self)
        self.p2 = port(master,v2,x+self.dx,y+self.dy,relation=type,label = 'Back Port',bind=self)
        self.visual = self.gui.create_oval(self.x-self.d-self.dx,self.y-self.d-self.dy,self.x+self.d+self.dx,self.y+self.d+self.dy,width=3)
        self.gui.tag_bind(self.visual,'<B1-Motion>',self.move)

    def move(self,event):
        self.x = event.x
        self.y = event.y
        self.gui.coords(self.visual,self.x-self.d-self.dx,self.y-self.d-self.dy,self.x+self.d+self.dx,self.y+self.d+self.dy)
        self.p1.move(self.x-self.dx,self.y-self.dy)
        self.p2.move(self.x+self.dx,self.y+self.dy)
        

    
        

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
        
        self.objects = []
        self.connect = None
        self.types = {'wire':[],
                      'dc battery':[],
                      'resistor':[],
                      'ac battery':[],
                      'inductor':[],
                      'capacitor':[]
                      }
        self.connect = None
        self.infoBox = self.gui.create_rectangle(0,0,0,0,fill='light yellow')
        self.infoText = self.gui.create_text(0,0,text='',anchor=CENTER)
        
   

    def showInfo(self,event,text):
        dy = 10*(text.count('\n')+1)
        data = text.split('\n')
        maxx = 0
        for i in data:
            if len(i)>maxx:
                maxx = len(i)
        dx = 3*maxx
        self.gui.itemconfig(self.infoText,text=text)
        self.gui.coords(self.infoText,event.x,event.y-50)
        self.gui.coords(self.infoBox,event.x-dx,event.y-dy-50,event.x+dx,event.y+dy-50)
    def hideInfo(self,event):
        self.gui.itemconfig(self.infoText,text='')
        self.gui.coords(self.infoText,0,0)
        self.gui.coords(self.infoBox,0,0,0,0)

    

   
        
                            
        

    
        
root = Tk()
board = LiveGUI(root)

obj(board,100,100,v1=15,v2=0,orientation='h')
obj(board,100,150,v1=15,v2=0)
obj(board,100,200,v1=15,v2=0)
obj(board,100,250,v1=15,v2=0)

mainloop()
    
   
