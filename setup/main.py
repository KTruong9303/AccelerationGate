from pickle import TRUE
import pygame, sys
from settings import *
from level import Level
import button
import random as rand

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 40)
trait_font = pygame.font.SysFont('Comic Sans MS', 20)

class Game:		
	"""
	A class store general setup 
	...
	Atributes:
		screen <class pygame.surface.Surface>: create a screen
		clock <class pygame.tiem.Clock>: create time
		level <class level.Level>: create objects
		background <class pygame.surface.Surface>: create background
	---------
	Methods
		run():
			run the game.
	-------
	"""																					
	def __init__(self):
		"""
		Constructs all the necessary attributes for the game.
		Parameters
			screen <class pygame.surface.Surface>: create a screen
			clock <class pygame.tiem.Clock>: create time
			level <class level.Level>: create objects
			background <class pygame.surface.Surface>: create background
		----------
			
		Returns
		-------
		None
		"""
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  #độ lớn màn hình
		pygame.display.set_caption('Acceleration Gate') #set caption         
		self.clock = pygame.time.Clock()         #thời gian
		self.level = Level()					 #level là gì?
		self.background = pygame.image.load("../graphics/map_co_ngu/final_map.png")

		self.game_paused = True
		self.load_button()
		self.menu_state = 'pick_trait'
		self.round = 0
		self.timer = -1
		
		self.A_picked = -1
		self.B_picked = -1
		
	def load_button(self):
		resume_img = pygame.image.load("../graphics/button/resume.png").convert_alpha()
		option_img = pygame.image.load("../graphics/button/option.png").convert_alpha()
		quit_img = pygame.image.load("../graphics/button/quit.png").convert_alpha()
		back_img = pygame.image.load("../graphics/button/back.png").convert_alpha()
		volume_img = pygame.image.load("../graphics/button/volume.png").convert_alpha()
		trait1_img = pygame.image.load("../graphics/button/trait1.png").convert_alpha()
		trait2_img = pygame.image.load("../graphics/button/trait2.png").convert_alpha()
		trait3_img = pygame.image.load("../graphics/button/trait3.png").convert_alpha()
		self.resume_button = button.Button(400,90,resume_img,1.5)
		self.option_button = button.Button(400,260,option_img,1.5)
		self.quit_button = button.Button(400,430,quit_img,1.5)
		self.back_button = button.Button(400,260,back_img,1.5)
		self.volume_button = button.Button(400,430,volume_img,1.5)
		self.trait1_button = button.Button(110,30,trait1_img,1)
		self.trait2_button = button.Button(110,230,trait2_img,1)
		self.trait3_button = button.Button(110,430,trait3_img,1)

###############################################################
	def run(self):
		"""
		create Game loop, run the game.
		Parameters
		-----------
		Returns
		--------
		None
		"""
		while True: #Gameloop
			self.screen.blit(self.background, (0, 0))
	#setting
			if self.game_paused == True:
				if self.menu_state == 'pick_trait':
					i = 6#rand.randint(1,8)
					if self.trait1_button.draw(self.screen):
						self.A_picked = i
					elif self.trait2_button.draw(self.screen):
						self.A_picked = (i+1)%8
					elif self.trait3_button.draw(self.screen):
						self.A_picked = (i+2)%8

					text_surface = trait_font.render(f'{TRAIT[i]}', False, (0, 0, 0))
					self.screen.blit(text_surface, (180,60)) 
					text_surface = trait_font.render(f'{TRAIT[(i+1)%8]}', False, (0, 0, 0))
					self.screen.blit(text_surface, (180,260))
					text_surface = trait_font.render(f'{TRAIT[(i+2)%8]}', False, (0, 0, 0))
					self.screen.blit(text_surface, (180,460))

					keys = pygame.key.get_pressed()
					
					if keys[pygame.K_1] :
						self.B_picked = i
					elif keys[pygame.K_2] :
						self.B_picked = (i+1)%8
					elif keys[pygame.K_3] :
						self.B_picked = (i+2)%8		
					
					if self.A_picked > -1 and self.B_picked > -1:
						self.level.get_trait(self.A_picked, self.B_picked)
						self.A_picked = -1
						self.B_picked = -1
						self.game_paused = False
						self.menu_state = 'main'
				elif self.menu_state == 'main':
					if self.resume_button.draw(self.screen):
						self.game_paused = False
					elif self.option_button.draw(self.screen):
						self.menu_state = 'option'
					elif self.quit_button.draw(self.screen):
						pygame.quit()
						sys.exit()
				elif self.menu_state == 'option':
					if self.back_button.draw(self.screen):
						self.game_paused = True
						self.menu_state = 'main'
					if self.volume_button.draw(self.screen):
						self.game_paused = True
			else:
	#bat dau round
				if 	self.timer < 0:
					if self.timer == -1:
						self.round += 1
					text_surface = my_font.render(f'ROUND {self.round} START!', False, (0, 0, 0))

					#SPAWN SPRITE HERE
					# self.level.spawn_creep(self.round)

					self.screen.blit(text_surface, (375,125))
					self.timer += 0.023					

	#continuous reality
				else:
		#timer	
					dt = self.clock.tick(600) / 1000   #delta time
					self.timer += 1/60#0.0083 # XAP XI 1/120
		#visualize timer
					text_surface = my_font.render(f'TIME: {31-round(self.timer)} s', False, (0, 0, 0))
					self.screen.blit(text_surface, (510,15))

		#Count down and pick trait
					if self.timer > 10:
						# declare ROUND 1
						if self.round > 1:
							# pick traits:
							pass
						print('TIME UP!')
						self.timer = -1
						self.game_paused = True
						self.menu_state = 'pick_trait'

					self.level.run(dt)    
					# pygame.display.flip()   #????

	#get input
			for event in pygame.event.get():  #exit game
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.game_paused = True
					if event.key == pygame.K_e:
						self.game_paused = False
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
		
	#update
			pygame.display.update()   #????

			

'=============Run the game====================================================='
import os
os.chdir('D:\VS_Code_file\python\IE221\RescureCity\_accelerationGate\setup_code')

if __name__ == '__main__':
	game = Game()
#####################################################
	# game.run()
	help(game)
	




'''
Game Cổng Gia Tốc [Acceleration Gate]
_______________________
|   	      		  |
|   	  \    	  o	  |
|   	   \ 		  |
|  o	    \		  |
|_____________________|
A: attack
D: Defense
Rule: 2 bên bắn nhau liên tục
	- có thanh máu 100
	- stop các round chọn skill: hồi máu, hút máu, đốt, sát thương, khế ước quỷ dữ, khiên, đạn phá đạn, đạn nổ tạo 1 vùng, đạn nổ tóe ra, tàn hình, tăng tốc độ di chuyển... 
Cốt truyện: 2 nhà Khoa học đại tài Vayce và Jiktor đã nghiên cứu thành công 1 cỗ máy có tên là hextech. Vayce muốn dùng cỗ máy này để giúp mọi người, còn Jiktor muốn sử dụng cỗ máy để cứu em gái mình. 2 bên xảy ra mâu thuẫn và quyết chiến với nhau.
DONE;
> tạo 2 nhân vật: di chuyển [y]
> map: hình ảnh, cổng gia tốc [y]
> bắn đạn [y]
> chịu sát thương -> hiển thị thanh máu [y]
> đạn qua cổng gia tốc [y]
> cơ chế tự động nhắm how about có cái cần chỉnh độ lên và độ xuống nhể -> ko bik [y]
> sub-menu : xem sau có code github [Y]
> clock đồng hồ -> hiển thị đồng hồ -> youtube [y]
> các round -> tự chế ik [y]
-> update kĩ năng: auto aim, double trouble -> shield, more sprite, more dame, more speed, more cooldown
-> tạo map 2 mùa: mùa khô và mùa nắng -> trong pydey valley
-> popup thanh chọn: -> làm như setting
> animation: đạn, vẽ map -> up hình vô [y]
-> deploy thành game -> how to exe
-> âm thanh -> kiếm âm thanh
-> làm slide
-> làm oop
-> up youtube
-> làm báo cáo
'''