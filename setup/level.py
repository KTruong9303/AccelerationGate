import pygame 
from settings import *
from player import *
from sprites import *
import random as rand

class Level:
	'''
	A class create and draw objects in game.
	...
	Atributes:
		display_surface  <class 'pygame.surface.Surface'>: 
		all_sprites <class 'pygame.sprite.Group'>: group contain all sprites
		collision_sprites <class 'pygame.sprite.Group'>: group contain sprite have collision
		bullet 	<class 'pygame.sprite.Group'>: group for bullet
		background  <class 'pygame.surface.Surface'>:  load background
	----------
	Methods:
		setup(): create objects in game: player, wall
		run(dt): draw all objects and update continously
	----------
	'''
	def __init__(self):
		'''
		Constructs all the necessary attributes for the game object.
		Atributes:
			display_surface  <class 'pygame.surface.Surface'>: 
			all_sprites <class 'pygame.sprite.Group'>: group contain all sprites
			collision_sprites <class 'pygame.sprite.Group'>: group contain sprite have collision
			bullet 	<class 'pygame.sprite.Group'>: group for bullet
			background  <class 'pygame.surface.Surface'>:  load background
		----------
		Return:
			None
		----------
		'''
		# get the display surface
		self.display_surface = pygame.display.get_surface() #take no argument
		# sprite groups
		self.all_sprites = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()
		self.bullet = pygame.sprite.Group()
		#background
		self.background = pygame.image.load("../graphics/map_co_ngu/final_map.png")
		## method: setup
		self.setup()      #tạo nhân vật

	def spawn_creep(self, round):
		'''
		function create creep every round
		'''
		self.wall1 = Clob((230+rand.randint(0,100),200),(40*round,25*round),[self.all_sprites,self.collision_sprites])


	def setup(self):
		'''
		A function declare all objects at the beginning contains: players, wall
		...
		Attributes:
			player1 <class Player>: create player 1
			player2 <class Player>: create player 2
			GATE <class sprites>: create accleration gate at the middle screen
			wall1 <class sprites>: create wall in the corner
			wall2 <class sprites>: create wall in the corner
			wall3 <class sprites>: create wall in the corner
			wall4 <class sprites>: create wall in the corner
		------------
		Return:
			None
		------------
		'''
		self.player1 = Keyboard_player((100,100), self.all_sprites, self.collision_sprites,self.bullet)
		self.player2 = Mouse_player((660,430), self.all_sprites, self.collision_sprites,self.bullet)
		self.GATE = Gate((625,335),[self.all_sprites,self.collision_sprites])
		
		# self.wall2 = Clob((0,620),(100,100),[self.all_sprites,self.collision_sprites])
		# self.wall3 = Clob((1180,0),(100,100),[self.all_sprites,self.collision_sprites])
		# self.wall4 = Clob((1180,620),(100,100),[self.all_sprites,self.collision_sprites])
	def get_trait(self,trait1,trait2):
		'''
		function update player skill
		'''
		self.player1.traits = trait1
		self.player2.traits = trait2
		self.player1.implement_traits()
		self.player2.implement_traits()
##############################################################################
	def run(self,dt):
		'''
		A function continously draw and update all objects per frame
		...
		Attributes:
			dt (float): 'delta time' as i understand it's frame
		Return:
			None
		'''

		self.all_sprites.draw(self.display_surface)  #???
		self.all_sprites.update(dt)  #???


