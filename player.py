import pygame
from settings import *
from support import import_folder
# import pygame_textinput
# from pygame_textinput import TextInput
import random as rand


class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group, obstacles,bullet):   #vị trí và camera
		super().__init__(group)
		#load the gif before 
		self.import_assets()
		self.status = 'left'
		self.frame_index = 1
		# general setup
		self.image = self.animations[self.status][self.frame_index]#image
		self.rect = self.image.get_rect(center = pos)
		self.old_rect = self.rect.copy()
		self.obstacles = obstacles
		self.bullet = bullet

		# movement attributes
		self.direction = pygame.math.Vector2()  #hướng đi
		self.pos = pygame.math.Vector2(self.rect.center)  #vị trí
		self.speed = 500
		self.cooldown = -1

		## self.heal = 100
		self.gr = group
		self.screen = pygame.display.get_surface()
		self.ratio = 1
		
	#animation of character
	def import_assets(self):
		#chứa gif
		self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[]}
		for animation in self.animations.keys():
			full_path = '../graphics/char/' + animation
			self.animations[animation] = import_folder(full_path)

######################################################################
	def animate(self,dt):
		self.frame_index += 4 * dt #tốc độ gif
		if self.frame_index >= len(self.animations[self.status]):
			self.frame_index = 0

		self.image = self.animations[self.status][int(self.frame_index)]

	#Nhận input từ bàn phím
	def input(self):
		keys = pygame.key.get_pressed()
		#hướng đi của character
		if keys[pygame.K_UP] :
			self.direction.y = -2
			self.status = 'up'
		elif keys[pygame.K_DOWN] :
			self.direction.y = 2
			self.status = 'down'
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT] :
			self.direction.x = 1
			self.status = 'right'
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			self.status = 'left'
		else:
			self.direction.x = 0
		
		click = pygame.mouse.get_pressed()
		current_time = pygame.time.get_ticks()
		
		if self.cooldown >= 0:
			self.cooldown -= 4
		if keys[pygame.K_SPACE]:
			if self.cooldown < 0:
				self.create_bullet()
				self.cooldown = 1000
		 
	#collision
	def collision(self):
		collision_sprites = pygame.sprite.spritecollide(self,self.obstacles, False)
		key = pygame.key.get_pressed()
		if collision_sprites:
				for sprite in collision_sprites:
					#collision on the right
					if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
						self.rect.right  = sprite.rect.left
						self.pos.x = self.rect.x
						
					#collision on the left
					if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
						self.rect.left  = sprite.rect.right
						self.pos.x = self.rect.x
						 	
					#collision on the bottom
					if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
						self.rect.bottom  = sprite.rect.top
						self.pos.y = self.rect.y
						
					#collision on the top
					if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
						self.rect.top  = sprite.rect.bottom
						self.pos.y = self.rect.y
					pygame.font.init()
					my_font = pygame.font.SysFont('Comic Sans MS', 30)
					if sprite.type == 'clob' and key[pygame.K_m]:	
						text_surface = my_font.render(f'Some Text: {self.num[i]}', False, (0, 0, 0))
						self.screen.blit(text_surface, (0,0))
					if sprite.type == 'gate' and key[pygame.K_n]:
						pass
	
	def window_collision(self):
			if self.rect.left < 0:
				self.rect.left = 0
				self.pos.x = self.rect.x
				self.direction.x *= -1
			if self.rect.right > 1280:
				self.rect.right = 1280
				self.pos.x = self.rect.x
				self.direction.x *= -1
		
			if self.rect.top < 0:
				self.rect.top = 0
				self.pos.y = self.rect.y
				self.direction.y *= -1
			if self.rect.bottom > 720:
				self.rect.bottom = 720
				self.pos.y = self.rect.y
				self.direction.y *= -1

	#lấy status
	def get_status(self): #kiem tra char co dung yen hay di chuyen
		if self.direction.magnitude() == 0:  #khong di chuyen
			self.status = self.status.split('_')[0] + '_idle'

	#di chuyển
	def move(self,dt):
		# normalizing a vector 
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		# horizontal movement
		self.pos.x += self.direction.x * self.speed * dt
		
		self.pos.y += self.direction.y * self.speed * dt
		#self.rect.centerx = round(self.pos.x)	
		self.rect.x = round(self.pos.x)	

		# vertical movement
		self.rect.y = self.pos.y
		self.collision()
		self.window_collision()

	def create_bullet(self):
		return Bullet(self.rect.center,[self.gr,self.bullet],self.obstacles,0)

	def health_bar(self,x,y,w,h,ratio):
		pygame.draw.rect(self.screen, 'red', (x,y,w,h))
		pygame.draw.rect(self.screen, 'green', (x,y,w*ratio,h))
	def get_damage(self):
		collision_sprites = pygame.sprite.spritecollide(self,self.bullet, False)
		
		for sprite in collision_sprites:
			if sprite.side == 1:
				self.ratio -= 0.01
		if self.ratio < 0:
			pygame.font.init()
			my_font = pygame.font.SysFont('Comic Sans MS', 30)
			text_surface = my_font.render(f'Game Over: Bear Win!', False, (0, 0, 0))
			self.screen.blit(text_surface, (500,0))
	

	def update(self, dt):
		self.old_rect = self.rect.copy()
		self.input()
		self.get_status()
		self.move(dt)
		self.animate(dt)
		self.health_bar(0,0,640,10,self.ratio)
		self.get_damage()

class Bullet(pygame.sprite.Sprite):
	def __init__(self, pos, group,obstacles,side):
		super().__init__(group)
		self.image = pygame.Surface((10,10))
		self.image.fill((0,255,255))
		self.rect = self.image.get_rect(center = pos)
		self.getmouse_pos = pygame.mouse.get_pos()
		self.side = side
		self.obstacles = obstacles
		self.group = group
		self.speed = 1000
		self.old_rect = self.rect.copy()
		self.direction = pygame.math.Vector2()  #hướng đi
		self.direct()

	
	def collision(self):
		collision_sprites = pygame.sprite.spritecollide(self,self.obstacles, False)
		#if self.rect.colliderect(self.obstacles.rect):
			# collision_sprites.append(self.obstacles)
		if collision_sprites:
			self.image = pygame.Surface((20,20))
			self.image.fill((0,255,0))
			self.speed = 2500
		#window
		if self.rect.left < 0 or self.rect.right > 1280 or self.rect.top < 0 or self.rect.bottom > 720:
			self.group[0].remove(self)


	def direct(self):
		# normalizing a vector 
		self.direction.x = self.getmouse_pos[0] - self.rect.x
		self.direction.y = self.getmouse_pos[1] - self.rect.y
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()


	def update(self,dt):
		self.old_rect = self.rect.copy()
		self.rect.x += self.direction.x * self.speed * dt
		self.rect.y += self.direction.y * self.speed * dt
		self.collision()
	

class NPC(Player):
	def __init__(self, pos, group, obstacles,bullet):   #vị trí và camera
		super().__init__(pos, group, obstacles,bullet)
		#load the gif before 
		self.import_assets()
		self.status = 'left'
		self.frame_index = 1

		# general setup
		self.image = self.animations[self.status][self.frame_index]#image
		self.rect = self.image.get_rect(center = pos)
		self.old_rect = self.rect.copy()
		self.obstacles = obstacles

		# movement attributes
		self.direction = pygame.math.Vector2()  #hướng đi
		self.pos = pygame.math.Vector2(self.rect.center)  #vị trí
		self.speed = 500
		self.cooldown = -1

		## self.heal = 100
		self.gr = group
	#animation of character
	def import_assets(self):
		#chứa gif
		self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[]}
		for animation in self.animations.keys():
			full_path = '../graphics/character/' + animation
			self.animations[animation] = import_folder(full_path)

######################################################################
	#Nhận input từ bàn phím
	def input(self):
		keys = pygame.key.get_pressed()
		#hướng đi của character
		if keys[pygame.K_w] :
			self.direction.y = -2
			self.status = 'up'
		elif keys[pygame.K_s] :
			self.direction.y = 2
			self.status = 'down'
		else:
			self.direction.y = 0

		if keys[pygame.K_d] :
			self.direction.x = 1
			self.status = 'right'
		elif keys[pygame.K_a] :
			self.direction.x = -1
			self.status = 'left'
		else:
			self.direction.x = 0
		
		click = pygame.mouse.get_pressed()
		current_time = pygame.time.get_ticks()
		
		if self.cooldown >= 0:
			self.cooldown -= 4
		if click == (1,0,0):
			if self.cooldown < 0:
				self.create_bullet()
				self.cooldown = 1000
	
	def create_bullet(self):
		return Bullet(self.rect.center,[self.gr,self.bullet],self.obstacles,1)

	def health_bar(self,x,y,w,h,ratio):
		pygame.draw.rect(self.screen, 'red', (x+640,y,w,h))
		pygame.draw.rect(self.screen, 'green', (1280-w*ratio,y,w*ratio,h))		 
	def get_damage(self):
		collision_sprites = pygame.sprite.spritecollide(self,self.bullet, False)
		for sprite in collision_sprites:
			if sprite.side == 0:
				self.ratio -= 0.01
		if self.ratio < 0:
			pygame.font.init()
			my_font = pygame.font.SysFont('Comic Sans MS', 30)
			text_surface = my_font.render(f'Game Over: Soldier Win!', False, (0, 0, 0))
			self.screen.blit(text_surface, (500,0))	 
	