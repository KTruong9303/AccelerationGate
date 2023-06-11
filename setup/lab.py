import pygame

pygame.init()

#define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Masks")

#define colours
BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#hide mouse cursor
# pygame.mouse.set_visible(False)
import os
os.chdir('D:\VS_Code_file\python\IE221\RescureCity\_accelerationGate\setup_code')


#create soldier
soldier = pygame.image.load("../graphics/character/down/0.png").convert_alpha()
soldier_rect = soldier.get_rect()
soldier_mask = pygame.mask.from_surface(soldier)
mask_image = soldier_mask.to_surface()

#game loop
run = True
while run:

  #update background
  screen.fill(BG)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  screen.blit(mask_image, (0, 0))
  #update display
  pygame.display.flip()

pygame.quit()