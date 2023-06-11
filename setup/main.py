import pygame, sys
from settings import *
from level import Level
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
			for event in pygame.event.get():  #exit game
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			dt = self.clock.tick() / 1000   #delta time
			self.screen.blit(self.background, (0, 0))
			self.level.run(dt)       
			# pygame.display.flip()   #????
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
-> cơ chế tự động nhắm how about có cái cần chỉnh độ lên và độ xuống nhể
-> circle collision
-> menu
-> tạo map 4 mùa
-> popup thanh chọn: pause
-> update kĩ năng 
-> animation: người, đạn, trụ, blah blah
-> clock đồng hồ -> hiển thị đồng hồ  
-> deploy thành game
-> full màn hình
'''