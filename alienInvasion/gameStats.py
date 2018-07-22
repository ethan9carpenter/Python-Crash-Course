
class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.resetStats()
        self.gameActive = False
        self.highScore = 0
        self.level = 1
    
    def resetStats(self):
        self.remainingShips = self.settings.shipLimit
        self.score = 0
        self.level = 1
