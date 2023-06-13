from pickle import TRUE
import pygame, sys
from settings import *
from level import Level
import button


pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

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
		self.background = pygame.image.load("../graphics/map.png")

		self.game_paused = False
		self.load_button()
		self.menu_state = 'main'
		self.round = 0
		self.timer = -1
		
		
	def load_button(self):
		resume_img = pygame.image.load("../graphics/button/resume.png").convert_alpha()
		option_img = pygame.image.load("../graphics/button/option.png").convert_alpha()
		quit_img = pygame.image.load("../graphics/button/quit.png").convert_alpha()
		back_img = pygame.image.load("../graphics/button/back.png").convert_alpha()
		volume_img = pygame.image.load("../graphics/button/volume.png").convert_alpha()
		self.resume_button = button.Button(300,90,resume_img,2)
		self.option_button = button.Button(300,300,option_img,2)
		self.quit_button = button.Button(300,470,quit_img,2)
		self.back_button = button.Button(300,250,back_img,2)
		self.volume_button = button.Button(300,400,volume_img,2)

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
				if self.menu_state == 'main':
					if self.resume_button.draw(self.screen):
						self.game_paused = False
					if self.option_button.draw(self.screen):
						self.menu_state = 'option'
					if self.quit_button.draw(self.screen):
						pygame.quit()
						sys.exit()
				if self.menu_state == 'option':
					if self.volume_button.draw(self.screen):
						self.game_paused = True
					if self.back_button.draw(self.screen):
						self.game_paused = True
						self.menu_state = 'main'
			else:
	#bat dau round
				if 	self.timer < 0:
					if self.timer == -1:
						self.round += 1
					text_surface = my_font.render(f'round {self.round} bat dau!', False, (0, 0, 0))
					#PICK TRAIT HERE
					#SPAWN SPRITE HERE
					self.screen.blit(text_surface, (500,0))
					self.timer += 0.0023					

	#continuous reality
				else:
		#timer	
					dt = self.clock.tick(120) / 1000   #delta time
					self.timer += 0.0083 # XAP XI 1/120
		#visualize timer
					text_surface = my_font.render(f'time: {31-round(self.timer)}', False, (0, 0, 0))
					self.screen.blit(text_surface, (500,0))

		#Count down and pick trait
					if self.timer > 10:
						# declare ROUND 1
						if self.round > 1:
							# pick traits:
							pass
						print('TIME UP!')
						self.timer = -1
						self.game_paused = True

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
	game.run()




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
-> tạo map 4 mùa: như trên chưa nghĩ ra các loại kĩ năng phù hợp
-> popup thanh chọn: pause phải có đồng hồ đã
-> animation: đạn, vẽ map
-> deploy thành game
-> full màn hình
'''