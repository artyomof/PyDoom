import imghdr
import my_globals
import os
from os import walk
import pygame
import sys
from pygame.locals import *
import game
import qust
if __name__ == '__main__':
	my_globals.init()
	Game = qust.Game(my_globals.App1)
	my_globals.App1.run()

