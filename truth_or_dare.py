from typing import Any
import tkIMG
from tkinter import *

class player:
    def __init__(self,name = 'Defualt',picture='C:/Users/trent/OneDrive/Desktop/CodeFiles/Python/truth_or_dare_pics/girl.png'):
        self.name = name
        self.picture = picture
        self.turn = False
        self.points = 0
    
    def change_name(self,name):
        self.name = name
    
    def change_pic(self,url):
        self.picture = url

    def change_turn(self):
        self.turn = not self.turn
    
    def add_point(self,n):
        self.points += n

    def __getattribute__(self):
        return self.name
    
    

class game:
    def __init__(self,name,*players):
        self.name = name
        self.players = players
        print(self.players)

trent = player()
game('name',trent)
    
    
