import imghdr
import os
from os import walk
import pygame
import sys
from pygame.locals import *
import game






class Game(game.App):
    def __init__(self):
        Game.Idiot = game.App()
        Level1 = game.Scene(caption= 'Level 1', bg_image = "vopros.jpg", Player = [True, 0, 900])
        Level1a = game.Object(300, 500, 'DA.png.', event="oncrash.py" )
        Level1b = game.Object(800,500,"no.png.", event="EventCrash.py")
        Level1.AddCollide(Level1b)
        Level1.AddObject(Level1b)
        #knopb = pygbutton.PygButton((800,500,108,75), "Da",)
        #knopa = pygbutton.PygButton((300,500,108,75), "Nasdasdasdasdadadet", bgcolor= "PURPLE",fgcolor= "Black",)
        Level1.AddCollide(Level1a)
        Level1.AddObject(Level1a)
        obj = game.Object(0,1000, "zemli.jpg")
        Level1.AddCollide(obj)
        Level1.AddObject(obj)
        txt = game.Text("Вы любите пайтон?", (100,100))
        Level1.AddObject(txt)







if __name__ == '__main__':
    Game()
    Game.Idiot.run()