import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self, settings, screen, stats):
        self.settings = settings
        self.screen = screen
        self.stats = stats
        
        self.screenRect = screen.get_rect()
        
        self.fontColor = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        self.setupAll()
       
    def setupScoreboard(self):
        """Create an image to display as the scoreboard"""
        roundedScore = int(round(self.stats.score, -1))
        scoreString = "{:,}".format(roundedScore)
        self.scoreImage = self.font.render(scoreString, True, self.fontColor,
                                         self.settings.backgroundColor)
        
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right-20
        self.scoreRect.top = 20
        
    def display(self):
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.screen.blit(self.levelImage, self.levelRect)
        self.remainingShips.draw(self.screen)
        
    def setupHighScore(self):
        """Create an image of the high score to display as the scoreboard"""
        roundedScore = int(round(self.stats.highScore, -1))
        scoreString = "High Score: "+"{:,}".format(roundedScore)
        self.highScoreImage = self.font.render(scoreString, True, self.fontColor,
                                         self.settings.backgroundColor)
        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.scoreRect.top
        
    def setupLevel(self):
        """Create an image of the level to display as the scoreboard"""
        self.levelImage = self.font.render("Lv. "+str(self.stats.level), True, self.fontColor,
                                           self.settings.backgroundColor)
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.top = self.scoreRect.bottom + 10
        self.levelRect.right = self.scoreRect.right
        
    def setupRemainingShips(self):
        """Create an image of the remaining ships to be displayed"""
        self.remainingShips = Group()
        
        for i in range(self.stats.remainingShips):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 10 + i * ship.rect.width
            ship.rect.y = 10
            self.remainingShips.add(ship)
        
    def setupAll(self):
        self.setupScoreboard()
        self.setupHighScore()
        self.setupLevel()
        self.setupRemainingShips()
        
        
        
        
        
        
        
        