import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep

class GameFunctions():
    
    def __init__(self, settings, screen, ship, bullets, playButton, stats, aliens, scoreboard):
        self.settings = settings
        self.screen = screen
        self.ship = ship
        self.bullets = bullets
        self.playButton = playButton
        self.stats = stats
        self.aliens = aliens
        self.scoreboard = scoreboard
        
    def checkEvents(self):
        #Perform actions when an event occurs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.checkKeydownEvents(event)
            elif event.type ==pygame.KEYUP:
                self.checkKeyupEvents(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.checkPlayButton()
    
    def checkKeydownEvents(self, event):
        #Perform actions when a key is pressed
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight=True
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft=True
        elif event.key == pygame.K_SPACE:
            self.fireBullet()
        elif event.key == pygame.K_q:
            sys.exit()
               
    def checkKeyupEvents(self, event):
        #Perform actions when a key is released
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = False    
    
    def fireBullet(self):
        #Fires a new Bullet if appropriate
        if len(self.bullets) < self.settings.maxBullets:
            self.bullets.add(Bullet(self.settings, self.screen, self.ship))
    
    def updateBullets(self):
        """Update the Group of bullets to reflect visual changes
        and delete any Bullet that has left the screen"""
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)
        self.checkCollisions()
        
    def checkCollisions(self):
        """Checks for collisions and automatically removes them because
        of the two parameters that are set to True"""
        initAlienLength = len(self.aliens)
        
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)    
        
        changeAlienLength = initAlienLength - len(self.aliens)
        
        self.checkHighScore()
        self.stats.score += self.settings.alienScore*changeAlienLength
        self.scoreboard.setupScoreboard()
            
        if len(self.aliens) == 0:
            self.settings.levelUp()
            self.stats.level += 1
            self.scoreboard.setupLevel()
            self.bullets.empty()
            self.createFleet()
    
    def updateScreen(self):
        #Refresh the screen to reflect changes to the game
        self.screen.fill(self.settings.backgroundColor)
        self.ship.blitme()
        self.scoreboard.display()
        
        for bullet in self.bullets.sprites():
            if self.stats.gameActive:
                bullet.drawBullet()
        self.aliens.draw(self.screen) 
        
        if not self.stats.gameActive:
            self.playButton.drawButton()
        
        pygame.display.flip()
    
    def getMaxAliensX(self, width):
        #Maximum number of Aliens that can fit Horizontally
        availableSpace = self.settings.screenWidth-2*width
        
        return int(availableSpace/(2*width))
    
    def getMaxAliensY(self, height):
        #Maximum number of Aliens that can fit vertically
        availableSpace=self.settings.screenHeight-3*height-self.ship.rect.height
        
        return int(availableSpace/(2*height))
    
    def createAlien(self, width, column, row):
        #Creates an Alien
        alien=Alien(self.settings, self.screen)
        alien.x=width+2*width*column
        alien.y=alien.rect.height+2*alien.rect.height*row
        
        alien.rect.x=alien.x
        alien.rect.y=alien.y
        
        self.aliens.add(alien)
     
    def createFleet(self):
        #Create a fleet of Aliens in the Group aliens
        rectangle=Alien(self.settings, self.screen).rect
        width = rectangle.width
        height = rectangle.height
        maxAliensX = self.getMaxAliensX(width)
        maxAliensY = self.getMaxAliensY(height)
        
        for column in range(maxAliensX):
            for row in range(maxAliensY):
                self.createAlien(width, column, row)
    
    def isAlienAtBottom(self):
        #Determines whether an Alien has reached the bottom of the screen
        screenBottom = self.screen.get_rect().bottom
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screenBottom:
                return True
        
    def updateAliens(self):
        #
        self.checkFleetEdges()
        self.aliens.update()
        
        if self.isAlienAtBottom() or pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.shipHit()
        
    def checkFleetEdges(self):
        """Determine if an Alien has reach the edge of the screen, 
        changing the direction of the fleet and moving the fleet down
        if appropriate."""
        for alien in self.aliens.sprites():
            if alien.isAtEdge():
                self.changeFleetDirection()
                break
    
    def changeFleetDirection(self):
        """Change the direction of the fleet and move the fleet down"""
        self.settings.alienSpeed *= -1
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleetDropSpeed
    
    def shipHit(self):
        """Determines and performs what will happen given the Ship
        has been hit"""
        
        if self.stats.remainingShips > 0:
            self.stats.remainingShips-=1
            
            self.aliens.empty()
            self.bullets.empty()
            
            self.scoreboard.setupRemainingShips()
            
            self.createFleet()
            self.ship.centerShip()
            
            sleep(.5)
        else:
            self.stats.gameActive=False
            pygame.mouse.set_visible(True)
    
    def checkPlayButton(self):
        """Checks to see if the mouse has clicked the PlayButton, and
        if appropriate, will begin a new game"""
        
        position=pygame.mouse.get_pos()
        
        if not self.stats.gameActive and self.playButton.rect.collidepoint(position):
            self.stats.resetStats()
            self.stats.gameActive=True
            
            self.aliens.empty()
            self.bullets.empty()
            
            self.scoreboard.setupAll()
            
            self.settings.loadSettings()
            
            self.createFleet()
            self.ship.centerShip()
            
            pygame.mouse.set_visible(False)
    
    def checkHighScore(self):
        if self.stats.score > self.stats.highScore:
            self.stats.highScore = self.stats.score
            self.scoreboard.setupHighScore()
        
        
    
    

