import pygame 
from settings import *
from player import *
from sprites import *

class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface() #take no argument
			
		# sprite groups
		self.all_sprites = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()
		self.bullet = pygame.sprite.Group()
		
		self.background = pygame.image.load("../graphics/map.png")
		

		self.setup()      #tạo nhân vật

	def setup(self):
		# Generic(
		# 	pos = (0,0),
		# 	surf = pygame.image.load('../graphics/world/Computer Science.png').convert_alpha(),
		# 	groups = self.all_sprites)
		self.player = Player((300,600), self.all_sprites, self.collision_sprites,self.bullet)
		self.player2 = NPC((600,360), self.all_sprites, self.collision_sprites,self.bullet)
		self.GATE = Gate((490,210),(300,300),[self.all_sprites,self.collision_sprites])
		self.wall1 = Clob((0,0),(100,100),[self.all_sprites,self.collision_sprites])
		self.wall2 = Clob((0,620),(100,100),[self.all_sprites,self.collision_sprites])
		self.wall3 = Clob((1180,0),(100,100),[self.all_sprites,self.collision_sprites])
		self.wall4 = Clob((1180,620),(100,100),[self.all_sprites,self.collision_sprites])
########################################################################
	def run(self,dt):
		# self.display_surface.fill('black')
		 #only color
		# for sprite in self.all_sprites.sprites():
		# 	pygame.draw.rect(self.display_surface,'orange',sprite.old_rect)
		self.all_sprites.draw(self.display_surface)  #???
		self.all_sprites.update(dt)  #???

