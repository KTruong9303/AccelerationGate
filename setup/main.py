import pygame, sys
from settings import *
from level import Level
class Game:																										
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  #độ lớn màn hình
		pygame.display.set_caption('Acceleration Gate') #set caption         
		self.clock = pygame.time.Clock()         #thời gian
		self.level = Level()					 #level là gì?

###############################################################
	def run(self):
		while True: #Gameloop
			for event in pygame.event.get():  #exit game
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				#if pause?
				#if new round
  
			dt = self.clock.tick() / 1000   #delta time
			print(dt)
			self.level.run(dt)       
			pygame.display.update()   #????


import os
os.chdir('D:\VS_Code_file\python\IE221\RescureCity\project\setup')


if __name__ == '__main__':
	game = Game()
	################
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
< tạo 2 nhân vật: di chuyển 
-> map: hình ảnh, cổng gia tốc -> chưa cần, chủ yếu cần collision của cái cổng -> rồi lấy ảnh đẹp đẹp trên mạng về, rồi kêu làm trên map tile
-> bắn đạn 
-> chịu sát thương
-> đạn qua cổng gia tốc
-> stop round
-> update kĩ năng
-> clock đồng hồ
-> pause
-> menu
'''