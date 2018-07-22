import pygame
from settings import Settings
from ship import Ship
from gameFunctions import GameFunctions
from pygame.sprite import Group
from gameStats import GameStats
from button import Button
from scoreboard import Scoreboard

def runGame():
    # Initializes game and window
    pygame.init()
    settings = Settings()
    
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, settings)
    bullets = Group()
    aliens = Group()
    stats = GameStats(settings)
    scoreboard = Scoreboard(settings=settings, stats=stats, screen=screen)
    playButton = Button(settings = settings, screen = screen, text = "Play")
    
    gameFunctions = GameFunctions(settings, screen, ship, bullets, playButton, stats, aliens, scoreboard)
    gameFunctions.createFleet()
            
    while True:
        gameFunctions.checkEvents()
        
        if stats.gameActive:
            ship.update()
            gameFunctions.updateBullets()
            gameFunctions.updateAliens()
            
        gameFunctions.updateScreen()

runGame()