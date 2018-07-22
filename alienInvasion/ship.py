import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load("/Users/footballnerd12/Desktop/Python Crash Course"
        +"/Python Crash Course/Textbook Resources/chapter_12/images/ship.bmp")
       
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        self.center=float(self.rect.centerx)
        
        self.movingRight=False
        self.movingLeft=False
        
        self.settings=settings

    def blitme(self):
        """Draws Ship at current location"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.center+=self.settings.shipSpeed
        if self.movingLeft and self.rect.left > self.screen_rect.left:
            self.center-=self.settings.shipSpeed
        
        self.rect.centerx=self.center
        
    def centerShip(self):
        self.center=self.screen_rect.centerx
        