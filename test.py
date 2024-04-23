import imghdr
import os
from os import walk
import pygame
import sys
from pygame.locals import *
import game
import my_globals
import qust
game.App.object_id = 0
game.App.scene_id = 1
game.App.scenes = []
screen = pygame.display.set_mode((1280, 960), RESIZABLE)