import pygame 
from settings import *
from player import Player
from player import Player2
from sprites import Gate

class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface() #take no argument

		# sprite groups
		self.all_sprites = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()

		self.setup()      #tạo nhân vật

	def setup(self):
		# Generic(
		# 	pos = (0,0),
		# 	surf = pygame.image.load('../graphics/world/Computer Science.png').convert_alpha(),
		# 	groups = self.all_sprites)
		self.player = Player((640,360), self.all_sprites, self.collision_sprites)
		#self.player2 = Player2((64,36), self.all_sprites)
		for i in range(0,500,50):
			self.wall = Gate((527 + i*0.5,110+i),(30,30),[self.all_sprites,self.collision_sprites])
########################################################################
	def run(self,dt):
		self.display_surface.fill('black')  #only color
		# for sprite in self.all_sprites.sprites():
		# 	pygame.draw.rect(self.display_surface,'orange',sprite.old_rect)
		self.all_sprites.draw(self.display_surface)  #???
		self.all_sprites.update(dt)  #???

