import pygbutton
import pygame
buttonObj = pygbutton.PygButton((50, 50, 60, 30), 'Button Caption')
while True: # main game loop
    for event in pygame.event.get(): # event handling loop
        if 'click' in buttonObj.handleEvent(event):
            pass # Do stuff in response to button click here.
buttonObj.draw(DISPLAYSURFACE) # where DISPLAYSURFACE was the Surface object returned from pygame.display.set_mode()