import imghdr
import os
import re
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
        Game.Level2Nepravilno = game.Text('Неправильно!', (800, 0))
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
    Game.Level2.AddObject(game.Text("1 базовая команда в python является ''print'' как она работает рассказано на сайте", (100,100),fontsize=36))
    Game.Level2.AddObject(game.Text("пора применить свои знания напишите свое имя!", (160,160),fontsize=36))
    Game.Level2a = game.Object(300, 500, 'DA.png.', event= "qust.print1()")
    Game.Level2b = game.Object(800, 500, "no.png.", event="EventCrash.py")
    Game.Level2.AddObject(Game.Level2a)
    Game.Level2.AddObject(Game.Level2b)

    my_globals.App1.TP.pos.y = 0
    my_globals.App1.TP.pos.x = 0
    my_globals.App1.scene = Game.Level2



def level2complete():
    Game.Level3 = game.Scene(caption='Level 3', bg_image="vopros.jpg", Player=[True, 0, 900])
    Game.obj3 = game.Object(0, 1000, "zemli.jpg")
    Game.Level3.AddCollide(Game.obj3)
    Game.Level3.AddObject(Game.obj3)
    Game.Level3.AddObject(
        game.Text("Так же пайтон умеет считать мат выражения!", (100, 100),
                  fontsize=36))
    Game.Level3.AddObject(game.Text("Примени свои знания и выведи на экран простое выражение 2+2", (160, 160), fontsize=36))
    Game.Level3a = game.Object(300, 500, 'DA.png.', event="qust.print2()")
    Game.Level3b = game.Object(800, 500, "no.png.", event="EventCrash.py")
    Game.Level3.AddObject(Game.Level3a)
    Game.Level3.AddObject(Game.Level3b)


def level3complete():
    Game.Level4 = game.Scene(caption='Level 4', bg_image="vopros.jpg", Player=[True, 0, 900])
    Game.obj4 = game.Object(0, 1000, "zemli.jpg")
    Game.Level4.AddObject(game.Text("На этом уровне мы научимся создавать переменные!", (100,100),fontsize=36))
    Game.Level4.AddObject(game.Text("Теперь создайте любую переменную она понадобится дальше!", (160,160),fontsize=36))
    Game.Level4.AddCollide(Game.obj4)
    Game.Level4.AddObject(Game.obj4)
    Game.Level4a = game.Object(300, 500, 'DA.png.', event="qust.print()")
    Game.Level4b = game.Object(800, 500, "no.png.", event="EventCrash.py")
    Game.Level4.AddObject(Game.Level4a)
    Game.Level4.AddObject(Game.Level4b)

def level4complete():
    Game.Level5 = game.Scene(caption='Level 5', bg_image="vopros.jpg", Player=[True, 0, 900])
    Game.obj5 = game.Object(0, 1000, "zemli.jpg")
    Game.Level5.AddCollide(Game.obj5)
    Game.Level5.AddObject(Game.obj5)

def print1():
    result = re.search('(print)\(([^)]*)', my_globals.App1.cons1.text[0])

    if result != None:
        Game.Level2.AddObject(game.Text(result.group(2), (800, 0)))
        Level2c = game.Object(1160, 820, 'door.png', CollideEvent="qust.level2complete()")
        Game.Level2.AddObject(Level2c)
        Game.Level2.AddCollide(Level2c)
        Game.Level2Nepravilno.kill()
    if result == None:
        Game.Level2.AddObject(Game.Level2Nepravilno)

def print2():
    result = re.search('(print)\(([^)]*)', my_globals.App1.cons1.text[0])

    if result != None:
        Game.Level3.AddObject(game.Text(str(eval(result.group(2))), (800, 0)))
        Level3c = game.Object(1160, 820, 'door.png', CollideEvent="qust.level3complete()")
        Game.Level3.AddObject(Level3c)
        Game.Level3.AddCollide(Level3c)
        Game.Level2Nepravilno.kill()
    if result == None:
        Game.Level3.AddObject(Game.Level2Nepravilno)



def print3():
    result = re.search('(print)\(([^)]*)', my_globals.App1.cons1.text[0])

    if result != None:
        Game.Level4.AddObject(game.Text(result.group(2), (800, 0)))
        Level4c = game.Object(1160, 820, 'door.png', CollideEvent="qust.level4complete()")
        Game.Level4.AddObject(Level4c)
        Game.Level4.AddCollide(Level4c)
        Game.Level2Nepravilno.kill()
    if result == None:
        Game.Level2.AddObject(Game.Level2Nepravilno)





