from tkinter import *
import os
import sys
import getpass
#from PIL import ImageTk, Image
from tkIMG import upload
import os

font = ('times new roman',12)
root = Tk()
root.title('Create Account')
parent = Canvas(root)
parent.pack()
img = upload('image1.png')#ImageTk.PhotoImage(Image.open("image1.png"))

background_label = Label(parent, image=img)
background_label.place(x=1,y=1)
mainloop()
