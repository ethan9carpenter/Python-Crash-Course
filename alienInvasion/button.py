import pygame.font

class Button():
    
    def __init__(self, screen, text):
        self.screen=screen
        self.screenRect=screen.get_rect()
        
        self.width=200
        self.height=50
        self.buttonColor=(0, 255, 0)
        self.fontColor= (255, 255, 255)
        self.font=pygame.font.SysFont(None, 48)
        
        self.rect=pygame.Rect(0, 0, self.width, self.height)
        self.rect.center=self.screenRect.center
        
        self.setText(text)
    
    def setText(self, text):
        """Turns text into an image and places it on the Button"""
        self.textImage=self.font.render(text, True, 
                        self.fontColor, self.buttonColor)
        self.textImageRect=self.textImage.get_rect()
        self.textImageRect.center=self.rect.center
    
    def drawButton(self):
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.textImage, self.textImageRect)
        





