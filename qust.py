import imghdr
import os
from os import walk
import pygame
import sys
from pygame.locals import *
import game
from main import my_globals




class Game():
    def __init__(self, App):
        Game.Level1 = game.Scene(caption= 'Level 1', bg_image = "vopros.jpg", Player = [True, 0, 900])
        Game.Level1a = game.Object(300, 500, 'DA.png.', event="qust.oncrash()")
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
        App.scene = Game.Level1

def oncrash():
    pygame.font.init()
    txx = game.Text("Молодец!!", (300,300))
    my_globals.App1.scene.AddObject(txx)
    Level1c = game.Object(1160, 820, 'door.png', CollideEvent="qust.level1complete()")
    my_globals.App1.scene.AddObject(Level1c)

def level1complete():
    Game.Level2 = game.Scene(caption= 'Level 2', bg_image = "vopros.jpg", Player = [True, 0, 900])
    Game.obj2 = game.Object(0,1000, "zemli.jpg")
    Game.Level2.AddCollide(Game.obj2)
    Game.Level2.AddObject(Game.obj2)
    my_globals.App1.TP.pos.y = 0
    my_globals.App1.TP.pos.x = 0
    my_globals.App1.scene = Game.Level2