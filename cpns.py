import pygame
import os
import game
from pygame.locals import *
import sys
import my_globals
try:
    game.assign_list('x ', 'xuy')
except:
    game.printz('неправильное значение', 36)
