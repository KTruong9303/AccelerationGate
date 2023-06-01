import pygame
from settings import *

class Gate(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image = pygame.image.load('../graphics/gate.png').convert_alpha()
        # self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.type = 'gate'

class Clob(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        #self.image = pygame.image.load('../graphics/R.png').convert_alpha()
        self.image = pygame.Surface(size)
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.type = 'clob'