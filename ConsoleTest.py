import os
import pygame
from pygame.locals import *
import sys
import game as g
import re
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 960), RESIZABLE)
pygame.init()
running = True
result = result = re.search('(a)', 'aaaaa')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 960), RESIZABLE)
parsed =    {'(xuy)\(([^)]*?)': ['print({}', [2]],
			'(spawn)(\([^)]*?)': []}
class cons(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Console.png')
		self.rect = self.image.get_rect(topleft=(0, 0))
		self.Console = pygame.sprite.GroupSingle()
		self.Console.add(self)
		self.text = ['']
		self.curr_line = 0
		self.curr_collumn = 0
	def Add_to(self, line, collumn, item):
		self.text[line] = self.text[line][:collumn] + item + self.text[line][collumn:]
		self.curr_collumn += 1
	def del_from(self, line, collumn):
		self.text[line] = self.text[line][:collumn-1] + self.text[line][collumn:]
		self.curr_collumn -= 1

	def call(self):
		self.Console.draw(screen)
	def writetofile(self, list, file):
		with open(file, 'w') as output:
			output.write('import pygame' + '\n')
			output.write('import os' + '\n')
			output.write('import game' + '\n')
			output.write('from pygame.locals import *' + '\n')
			output.write('import sys' + '\n')
			for row in list:
				output.write(str(row) + '\n')
	def parse(self):
		nulls = []
		new = []
		for rows in range(len(self.text)):
			curr_null = 0
			while self.text[rows][curr_null] == ' ':
				curr_null += 1
			nulls.append(curr_null)
		for rows in self.text:
			new.append(rows)
		for row in range(len(new)):
			for i in parsed:
				if re.search(i, new[row]) != None:
					result = re.search(i, new[row])
					changables = []
					for j in parsed[i][1]:
						changables.append(result.group(j))
					new[row] = re.sub(i, parsed[i][0].format(*changables), new[row])
		for row in range(len(new)):
			self.text[row] = nulls[row]*' ' + new[row]


ConsoleCalled = False
cons1 = cons()
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		if event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				ConsoleCalled = not ConsoleCalled
			if ConsoleCalled:
				if event.key == pygame.K_RETURN:
					prev_line_tabs = ''
					for i in cons1.text[cons1.curr_line]:
						if i == ' ':
							prev_line_tabs += ' '
						else:
							break
					cons1.text.append('')
					cons1.curr_line += 1
					cons1.text[cons1.curr_line] = cons1.text[cons1.curr_line] + prev_line_tabs
				elif event.key == pygame.K_TAB:
					cons1.text[cons1.curr_line] = ' '*4 + cons1.text[cons1.curr_line]
					cons1.curr_collumn += 4
				elif event.key == pygame.K_BACKSPACE:
					cons1.del_from(cons1.curr_line, cons1.curr_collumn)
				elif event.key == pygame.K_LEFT:
					cons1.curr_collumn -= 1
					if cons1.curr_collumn < 0:
						cons1.curr_collumn = 0
						if cons1.curr_line <= 1:
							cons1.curr_line -= 1
				elif event.key == pygame.K_RIGHT:
					cons1.curr_collumn += 1
					if cons1.curr_collumn > len(cons1.text[cons1.curr_line]):
						if cons1.curr_line < len(cons1.text):
							cons1.curr_collumn = 0
							cons1.curr_line += 1
						else:
							curr_collumn = len(cons1.text[cons1.curr_line])
				elif event.key == pygame.K_UP:
					cons1.curr_line -= 1
					if cons1.curr_line < 0:
						cons1.curr_line = 0
						cons1.curr_collumn = 0
					else:
						if cons1.curr_collumn > len(cons1.text[cons1.curr_line]):
							cons1.curr_collumn = len(cons1.text[cons1.curr_line])
				elif event.key == pygame.K_DOWN:
					cons1.curr_line += 1
					if cons1.curr_line >= len(cons1.text):
						cons1.curr_line -= 1
						cons1.curr_collumn = len(cons1.text[cons1.curr_line])
					elif cons1.curr_collumn > len(cons1.text[cons1.curr_line]):
						cons1.curr_collumn = len(cons1.text[cons1.curr_line])
				elif event.key != pygame.K_ESCAPE:
					cons1.Add_to(cons1.curr_line, cons1.curr_collumn, event.unicode)
	screen.fill((255, 255, 255))

	if ConsoleCalled:
		cons1.call()
	clock.tick(30)
	for i in cons1.text:
		print(i)
	pygame.display.flip()
cons1.parse()
cons1.writetofile(cons1.text, 'cpns.py')
exec(open('cpns.py').read())
pygame.quit()
sys.exit()
