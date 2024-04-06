from game import *
class Demo(App):
	def __init__(self):
		super().__init__()
		App()
		Scene(caption='Intro')
		Text('Scene 0', (250, 440))
		Text('Introduction screen the app', (250, 300))

		Scene(bg=Color('yellow'), caption='Options', bg_img = 'nigga.png')
		Text('Scene 1', (250, 440))
		Text('Option screen of the app', (250, 300))
		App.scenes[1].draw()

		Scene(bg=Color('green'), caption='Main')
		Text('Scene 2', (250, 440))
		Text('Main screen of the app', (250, 300))

		App.scene = App.scenes[2]

if __name__ == '__main__':
	Demo().run()