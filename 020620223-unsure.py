import os
import sys
from tkinter import *
import matplotlib as mpl
import PIL as pil
import csv
import webbrowser as wb

class customSTD:
    def __init__(self,text):
        self.text = text
    def write(self,x):
        self.text.delete(0.0,END)
        self.text.insert(INSERT,x)
        
def bash():
    print('yo')
    text.after(100,lambda x='yoyo': print(x))
    
root = Tk()
bashText = Text(root)
bashText.pack()

text = Text(root)
text.pack()
scribe = customSTD(text)
sys.stdout = scribe
text.after(100,bash)
mainloop()
