import imghdr
import os
from os import walk
import pygame
import sys
from pygame.locals import *
import game
import my_globals





class Game(game.App):
    def __init__(self):
        Game.Level1 = game.Scene(caption= 'Level 1', bg_image = "vopros.jpg", Player = [True, 0, 900])
        Game.Level1a = game.Object(300, 500, 'DA.png.', event="oncrash.py" )
        Game.Level1b = game.Object(800,500,"no.png.", event="EventCrash.py")
        Game.Level1.AddCollide(Game.Level1b)
        Game.Level1.AddObject(Game.Level1b)
        Game.Level1.AddCollide(Game.Level1a)
        Game.Level1.AddObject(Game.Level1a)
        Game.obj = game.Object(0,1000, "zemli.jpg")
        Game.Level1.AddCollide(Game.obj)
        Game.Level1.AddObject(Game.obj)
        Game.txt = game.Text("Вы любите пайтон?", (100,100))
        Game.Level1.AddObject(Game.txt)




if __name__ == '__main__':
    Game = Game()
    my_globals.App1.run()
