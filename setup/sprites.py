import pygame
from settings import *
from support import *

class Gate(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        #load the gif before
        self.import_assets()
        self.frame_index = 1
        ###        
        self.screen = pygame.display.get_surface()
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        # self.rect = pygame.draw.circle(self.screen, 'red', pos, 360)
        # pygame.draw.circle(self.image, 'red', (200,200), 5)
        self.old_rect = self.rect.copy()
        self.type = 'gate'
        
    def import_assets(self):
		#chứa gif
        self.animations = []
        full_path = '../graphics/gate/'
        self.animations = import_folder2(full_path)
    def animate(self,dt):
        self.frame_index += 20 * dt #tốc độ gif
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = self.animations[int(self.frame_index)]
    def update(self,dt):
        self.animate(dt)

class Clob(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        #self.image = pygame.image.load('../graphics/R.png').convert_alpha()
        self.image = pygame.Surface(size)
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.type = 'clob'