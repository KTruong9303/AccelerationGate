import pygame
from settings import *
from support import *
import random as rand

class Gate(pygame.sprite.Sprite):
    '''
    A class to draw object Gate and its collision
    Attributes:
        frame_index (int): index for image in the asset        
        screen <class pygame.surface.Surface>: get the screen surface 
        image <class pygame.surface.Surface>: image of gate
        rect <class pygame.rect.Rect>: rectangle of gate
        mask <class pygame.mask>: mask of the image 
        old_rect <class pygame.rect.Rect>: old rectangle to know if collision and what direction
    Methods:
        import_assets: import the assets to player
        animate: change the image from assets continously to look more lively
        update: update the gate image
    '''
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

class Clob(Gate):
    '''
    A class of creeps
    Attribute: inherit from Gate
        size (tuple): to set the image size
        direction (Vector2): to set the direction 
    Methods:
        window_collision: to get collision with window
        move: to automatically move the creep
        update: update the creep state
    '''
    def __init__(self, pos, size, groups):
        self.size = size
        super().__init__(pos,groups)
        # self.import_assets()
        self.frame_index = 0
        #self.image = pygame.image.load('../graphics/R.png')        
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.direction.x = 1
        self.direction.y = 1

    def import_assets(self):
		#chứa gif
        self.animations = []
        full_path = '../graphics/round ghost/round ghost walk'
        self.animations = import_folder3(full_path,self.size)
    
    def widow_collision(self):
        '''
		A function that prevent player go outside of the screen
		Parameters:
		Return:
			None
		'''
        if self.rect.left < 96:			
            self.rect.left = 96
            self.pos.x *= self.rect.x
            self.direction.x *= -1
        if self.rect.right > 1152:
            self.rect.right = 1152
            self.pos.x = self.rect.x
            self.direction.x *= -1
		
        if self.rect.top < 64:
            self.rect.top = 64
            self.pos.y = self.rect.y
            self.direction.y *= -1
        if self.rect.bottom > 640:
            self.rect.bottom = 640
            self.pos.y = self.rect.y
            self.direction.y *= -1
        
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
    def move(self):
        self.pos.x += self.direction.x * 10 
        self.pos.y += self.direction.y * 10 
        self.rect.x = round(self.pos.x)	
        self.rect.y = round(self.pos.y)
        self.widow_collision()
            
    def update(self,dt):
        self.animate(dt)
        self.move()