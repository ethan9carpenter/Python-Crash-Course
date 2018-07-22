import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen=screen
        self.settings=settings
        
        self.image=pygame.image.load("/Users/footballnerd12/Desktop/"+
                                     "Python Crash Course/Python Crash Course/Textbook Resources/chapter_13/images/alien.bmp")
        self.rect=self.image.get_rect()
        
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        self.x=float(self.rect.x)
                
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        self.x+=self.settings.alienSpeed*self.settings.fleetDirection
        self.rect.x=self.x
        
    def isAtEdge(self):        
        return self.rect.right >= self.screen.get_rect().right or self.rect.left <= 0
        
        