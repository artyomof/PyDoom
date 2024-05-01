# обновлен мув, апдейт, джамп и инит у плеера, основной цикл, добавлена новая функция у плеера
# обновлены импорты
#
import imghdr
import os
from os import walk
import pygame
import sys
from pygame.locals import *
import re

vec = pygame.math.Vector2
HEIGHT = 960
WIDTH = 1280
clock = pygame.time.Clock()
ACC = 0.5
FRIC = -0.12
parsed = {'(print)\(([^)]*)': ['game.printz(my_globals.{})', [2]], '([^=]*)(=)(.*)': ['game.assign_x(\'{}\',{})', [1,3]]}

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def assign_x(x, y):
	print('did!')
	f = open('my_globals.py', 'a')
	f.write('\n{} = \'{}\''.format(x,y)) 

def printz(x):
	new_obj = Text(x, (0, 800))
	App.scene.printable.add(new_obj)



class App:
    def __init__(self):
        pass
    def selfinit(self):
        App.TP = Player("C:/PyDoom/test/Warrior_Idle_1.png", 0, 0, animation_folder='C:/PyDoom/test')
        App.Player = pygame.sprite.GroupSingle()
        App.object_id = 0
        App.flags = RESIZABLE
        Obj = Object(0, HEIGHT, 'platform1.png')
        App.running = True
        App.scenes = []
        App.Mouse = pygame.sprite.GroupSingle()
        App.scene_id = 0
        App.scene = Scene(Player=[True, 0, 0], bg=Color('black'), caption='Yappy door')
        App.scene.objects.add(Obj)
        App.scene.AddCollide(Obj)
        App.cons1 = cons()
        App.ConsoleCalled = False
        pygame.font.init()
        print('New App!')

    def init2(self):
        pygame.init()
        App.screen = pygame.display.set_mode((1280, 960), App.flags)
    def do_shortcut(self, event):
        k = event.key
        m = event.mod
        if k == K_x and m & KMOD_LMETA:
            print("cmd+X")
        elif k == K_x and m & KMOD_LALT:
            print("alt+X")
        elif k == K_x and m & KMOD_LCTRL:
            print("ctrl+X")
        elif k == K_x and m & KMOD_LMETA + KMOD_LSHIFT:
            print("cmd+shift+X")
        elif k == K_x and m & KMOD_LMETA + KMOD_LALT:
            print("cmd+alt+X")
        elif k == K_x and m & KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT:
            print("cmd+alt+shift+X")
        elif k == KMOD_LCTRL and m & KMOD_ENTER:
            if App.ConsoleCalled:
                App.cons1.parse()
                App.cons1.writetofile(App.cons1.text, 'cpns.py')
                App.cons1.text = ['']

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                if event.type == MOUSEBUTTONDOWN:
                    for i in App.scene.objects:
                        if i.rect.collidepoint(App.mouse):
                            i.CallEvent()
                if event.type == KEYDOWN:
                    App.do_shortcut(self, event)
                    if event.key == pygame.K_SPACE:
                        App.TP.jump()
                    if event.key == pygame.K_ESCAPE:
                    
                        if App.ConsoleCalled == True:
                            App.cons1.parse()
                            App.cons1.writetofile(App.cons1.text, 'cpns.py')
                            App.cons1.text = ['']
                            os.system('python cpns.py')
                        App.ConsoleCalled = not App.ConsoleCalled
                    if App.ConsoleCalled:
                        if event.key == pygame.K_RETURN:
                            prev_line_tabs = ''
                            for i in App.cons1.text[App.cons1.curr_line]:
                                if i == ' ':
                                    prev_line_tabs += ' '
                                else:
                                    break
                            App.cons1.text.append('')
                            App.cons1.curr_line += 1
                            App.cons1.text[App.cons1.curr_line] = App.cons1.text[App.cons1.curr_line] + prev_line_tabs
                        elif event.key == pygame.K_TAB:
                            App.cons1.text[App.cons1.curr_line] = ' ' * 4 + App.cons1.text[App.cons1.curr_line]
                            App.cons1.curr_collumn += 4
                        elif event.key == pygame.K_BACKSPACE:
                            App.cons1.del_from(App.cons1.curr_line, App.cons1.curr_collumn)
                        elif event.key == pygame.K_LEFT:
                            App.cons1.curr_collumn -= 1
                            if App.cons1.curr_collumn < 0:
                                if App.cons1.curr_line > 0:
                                    App.cons1.curr_line -= 1
                                    App.cons1.curr_collumn = len(App.cons1.text[App.cons1.curr_line])
                                else:
                                	App.cons1.curr_collumn = 0
                        elif event.key == pygame.K_RIGHT:
                            App.cons1.curr_collumn += 1
                            if App.cons1.curr_collumn > len(App.cons1.text[App.cons1.curr_line]):
                                if App.cons1.curr_line < len(App.cons1.text)-1:
                                    App.cons1.curr_collumn = 0
                                    App.cons1.curr_line += 1
                                else:
                                    curr_collumn = len(App.cons1.text[App.cons1.curr_line])
                        elif event.key == pygame.K_UP:
                            App.cons1.curr_line -= 1
                            if App.cons1.curr_line < 0:
                                App.cons1.curr_line = 0
                                App.cons1.curr_collumn = 0
                            else:
                                if App.cons1.curr_collumn > len(App.cons1.text[App.cons1.curr_line]):
                                    App.cons1.curr_collumn = len(App.cons1.text[App.cons1.curr_line])
                        elif event.key == pygame.K_DOWN:
                            App.cons1.curr_line += 1
                            if App.cons1.curr_line >= len(App.cons1.text):
                                App.cons1.curr_line -= 1
                                App.cons1.curr_collumn = len(App.cons1.text[App.cons1.curr_line])
                            elif App.cons1.curr_collumn > len(App.cons1.text[App.cons1.curr_line]):
                                App.cons1.curr_collumn = len(App.cons1.text[App.cons1.curr_line])
                        elif event.key != pygame.K_ESCAPE:
                            App.cons1.Add_to(App.cons1.curr_line, App.cons1.curr_collumn, event.unicode)
            App.mouse = pygame.mouse.get_pos()
            App.TP.moving_left = False
            App.TP.moving_right = False
            App.TP.move()
            App.cons1.draw()
            App.scene.draw()
            if App.TP.animation:
                if App.TP.jumping:
                    if App.TP.moving_left:
                        App.TP.image = pygame.transform.flip(App.TP.animation[0][App.TP.curr_jump], True, False)
                        App.TP.curr_jump += 1
                    else:
                        App.TP.image = App.TP.animation[0][App.TP.curr_jump]
                        App.TP.curr_jump += 1
                    print('jumped')
                    if App.TP.curr_jump >= len(App.TP.animation[0]):
                        App.TP.curr_jump = 0
                elif App.TP.moving_left:
                    App.TP.image = pygame.transform.flip(App.TP.animation[1][App.TP.curr_left], True, False)
                    App.TP.curr_left += 1
                    print('left')
                    if App.TP.curr_left >= len(App.TP.animation[1]):
                        App.TP.curr_left = 0
                elif App.TP.moving_right:
                    App.TP.image = App.TP.animation[1][App.TP.curr_right]
                    App.TP.curr_right += 1
                    print('right')
                    if App.TP.curr_right >= len(App.TP.animation[1]):
                        App.TP.curr_right = 0
                else:
                    App.TP.image = App.TP.afk
                    App.TP.curr_right = 0
                    App.TP.curr_left = 0
                    App.TP.curr_jump = 0
            for i in App.scene.objects:
            	if App.TP.rect.colliderect(i.rect):
            		i.DoCollide()
            mouse_now = Text(str(App.mouse), (App.mouse[0] + 10, App.mouse[1]), fontsize=24, color=(146, 110, 174))
            App.Mouse.add(mouse_now)
            App.Mouse.update()
            App.Mouse.draw(App.screen)
            App.TP.update()
            clock.tick(60)
        pygame.quit()
        sys.exit()


## qust.do1

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, filename=None, name=None, event=None, CollideEvent = None):
        pygame.sprite.Sprite.__init__(self)
        self.event = event
        self.id = App.object_id
        self.CollideEvent = CollideEvent
        App.object_id += 1
        if name == None:
            self.name = 'Object {}'.format(self.id)
        else:
            self.name = name
        if filename:
            self.image = pygame.image.load(filename)
            self.rect = self.image.get_rect(bottomleft=(x, y))

    def __str__(self):
        return self.name

    def CallEvent(self):
        if self.event != None:
            exec(self.event)

    def DoCollide(self):
        if self.CollideEvent != None:
            exec(self.CollideEvent)

class Player(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, animation_folder=None):
        pygame.sprite.Sprite.__init__(self)
        self.afk = pygame.image.load(filename)
        self.image = self.afk
        self.rect = self.image.get_rect()
        self.pos = vec((x, y))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.moving_left = False
        self.moving_right = False
        self.jumping = False
        if animation_folder != None:
            self.curr_left = 0
            self.curr_right = []
            self.curr_jump = []
            self.sub_folders = [name for name in os.listdir(animation_folder) if
                                os.path.isdir(os.path.join(animation_folder, name))]
            for i in self.sub_folders:
                if 'right' in i:
                    self.animation_folder_right = [name for name in os.listdir(animation_folder + '/' + i)]
                    for j in self.animation_folder_right:
                        self.curr_right.append(pygame.image.load(animation_folder + '/' + i + '/' + j))
                elif 'jump' in i:
                    self.animation_folder_jump = [name for name in os.listdir(animation_folder + '/' + i)]
                    for j in self.animation_folder_jump:
                        self.curr_jump.append(pygame.image.load(animation_folder + '/' + i + '/' + j))
            self.animation = [self.curr_jump, self.curr_right]
            for i in self.animation:
                print(i)
            self.curr_right = 0
            self.curr_left = 0
            self.curr_jump = 0

    def move(self):
        self.acc = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.bottomleft = self.pos

    def jump(self):
        hits = pygame.sprite.spritecollide(App.TP, App.scene.Collidable_Objects, False)
        if hits:
            self.vel.y -= 15
            self.jumping = True

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.moving_left = True
            self.moving_right = False
        if pressed_keys[K_RIGHT]:
            self.moving_left = False
            self.moving_right = True
        for i in App.scene.Collidable_Objects:
            if pygame.Rect.colliderect(App.TP.rect, i.rect) and App.TP.rect.bottom >= i.rect.top + 1:
                self.pos.y = i.rect.top + 1
                self.vel.y = 0
                self.jumping = False
            elif pygame.Rect.colliderect(App.TP.rect, i.rect) and (App.TP.rect.left <= i.rect.right + 1) and (
                    App.TP.rect.left > i.rect.left):
                self.pos.x = i.rect.right + 1
                self.jumping = False
            elif pygame.Rect.colliderect(App.TP.rect, i.rect) and (App.TP.rect.right >= i.rect.left + 1) and (
                    App.TP.rect.right <= i.rect.right + 1):
                self.pos.x = i.rect.left - App.TP.rect.width + 1
                self.jumping = False
            elif pygame.Rect.colliderect(App.TP.rect, i.rect) and (App.TP.rect.top <= i.rect.bottom + 1):
                self.pos.y = i.rect.bottom - App.TP.rect.height + 1
                self.jumping = False


class Text(pygame.sprite.Sprite):
    def __init__(self, text, pos, fontsize=72, color='white'):
        pygame.sprite.Sprite.__init__(self)
        self.event = None
        self.CollideEvent = None
        self.font = pygame.font.SysFont("Arial", fontsize)
        self.textSurf = self.font.render(text, 1, color)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.pos = tuple(pos)
        self.image = pygame.Surface((W, H))
        textrect = self.textSurf.get_rect(center=self.image.get_rect().center)
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.textSurf, textrect)
        self.rect = self.image.get_rect(topleft=pos)


    def draw(self):
        self.image.blit(self.textSurf, self.pos)


    def CallEvent(self):
        if self.event != None:
            exec(self.event)


    def DoCollide(self):
        if self.CollideEvent != None:
            exec(self.CollideEvent)


class Scene():
    ## Player = [True, x, y]
    def __init__(self, bg=Color('gray'), caption='Unnamed Scene', Player=[False], **options):
        
        App.scenes.append(self)
        App.scene = self
        App.scene.writable = pygame.sprite.Group()
        App.scene.printable=pygame.sprite.GroupSingle()
        self.id = App.scene_id
        App.scene_id += 1
        self.bg = bg
        self.objects = pygame.sprite.Group()
        self.caption = caption
        self.file = options.get('bg_image', 0)
        self.Collidable_Objects = pygame.sprite.Group()
        self.Text = []
        if Player[0]:
            App.TP.rect.topleft = vec((Player[1], Player[2]))
            App.Player.update()
        if self.file:
            self.image = pygame.image.load(self.file)
            size = App.screen.get_size()
            self.image = pygame.transform.smoothscale(self.image, size)
        else:
            print('Wrong bg_image name at Scene {} or image dont given'.format(self.id))

    def AddObject(self, *objects):
        for i in objects:
            self.objects.add(i)

    def DelObject(self, **options):
        if options.get('id', 0):
            for i in self.objects:
                if i.id == options.get('id'):
                    self.objects.remove(i)
        if options.get('name', 0):
            for i in self.objects:
                if i.name == options.get('name'):
                    self.objects.remove(i)

    def AddCollide(self, *objects):
        for i in objects:
            self.Collidable_Objects.add(i)

    def draw(self):
        for i in self.Text:
            i.draw()
        pygame.display.set_caption(self.caption)
        self.objects.update()
        self.objects.draw(App.screen)
        App.scene.writable.update()
        App.scene.writable.draw(App.screen)
        App.scene.printable.update()
        App.scene.printable.draw(App.screen)
        pygame.display.update()
        try:
            App.screen.blit(self.image, (0, 0))
        except:
            App.screen.fill(self.bg)
        try:
            App.Player.add(App.TP)
            App.Player.update()
            App.Player.draw(App.screen)

        except:
            pass

    def __str__(self):
        return 'Scene {}'.format(self.id)


class cons(pygame.sprite.Sprite, App):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Console.png')
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.Console = pygame.sprite.GroupSingle()
        self.Console.add(self)
        self.strings = []
        self.text = ['']
        self.curr_line = 0
        self.curr_collumn = 0

    def draw(self):
        App.scene.writable = pygame.sprite.Group()
        for i in self.strings:
        	i.kill()
        self.strings = []
        curr_pos_of_text = [0, 0]
        for i in self.text:
            if self.text.index(i) == self.curr_line:
                pen = self.text[self.curr_line][:self.curr_collumn] + '|' + self.text[self.curr_line][self.curr_collumn:]
                App.scene.writable.add(Text(pen, curr_pos_of_text))
            else:
                App.scene.writable.add(Text(i, curr_pos_of_text))
                self.strings.append(Text(i, curr_pos_of_text))
                curr_pos_of_text[1] += Text(i, curr_pos_of_text).textSurf.get_height()
            print(i)
        App.scene.writable.update()

    def Add_to(self, line, collumn, item):
        self.text[line] = self.text[line][:collumn] + item + self.text[line][collumn:]
        self.curr_collumn += 1

    def del_from(self, line, collumn):
        self.text[line] = self.text[line][:collumn - 1] + self.text[line][collumn:]
        self.curr_collumn -= 1
        
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
            self.text[row] = nulls[row] * ' ' + new[row]


if __name__ == "__main__":
    App().run()
