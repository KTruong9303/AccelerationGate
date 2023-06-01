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
		self.background = pygame.image.load("../graphics/map.png")
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
			# print(dt)
			self.screen.blit(self.background, (0, 0))
			self.level.run(dt)       
			pygame.display.flip()   #????
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
> tạo 2 nhân vật: di chuyển [y]
> map: hình ảnh, cổng gia tốc [y]
> bắn đạn [y]
> chịu sát thương -> hiển thị thanh máu [y]
> đạn qua cổng gia tốc [y]
-> pause
-> cơ chế tự động nhắm how about có cái cần chỉnh độ lên và độ xuống nhể
-> menu
-> full màn hình
-> animation: người, đạn, trụ, blah blah
-> update kĩ năng 
-> clock đồng hồ -> hiển thị đồng hồ  
-> deploy thành game
-> câu đố
----------
game có 4 trụ 4 góc và cổng gia tốc hình trụ ở giữa
-> bấm vào hiện ra bảng -> tạo ra bài toán -> nhận input
xong rồi phải đi giải từng trụ để lấy đủ 3 key thì mở đc cổng và chạy trốn hoặc là phải solokill đối phương
giờ nè -> key variable
game này 2 người chơi còn train máy hơi khó
giờ 2 người di chuyển thì ez nè
rồi bắn đạn thì đổi cơ chế, ko bắn theo chuột nữa mà nhắm tự động 
'''