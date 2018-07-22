from json import load as jsonLoad

class Settings():
    """Controls settings for Alien Invasion"""
    
    def __init__(self):
        self.loadSettings()
        
    def loadSettings(self):
        fileName="/Users/footballnerd12/Desktop/Python Crash Course/Python Crash Course/alienInvasion/alienInvasionSettings.json"
        
        with open(fileName, "r") as settings:
            contents = jsonLoad(settings)
            self.bulletSpeed=contents["bulletSpeed"]
            self.shipSpeed=contents["shipSpeed"]
            self.alienSpeed=contents["alienSpeed"]
            self.alienScore=contents["alienScore"]
            self.nextLevelSpeedFactor=contents["nextLevelSpeedFactor"]
            self.scoreIncreaseFactor=contents["scoreIncreaseFactor"]
            self.screenWidth=contents["screenWidth"]
            self.screenHeight=contents["screenHeight"]
            self.backgroundColor=contents["backgroundColor"]
            self.shipLimit=contents["shipLimit"]
            self.bulletWidth=contents["bulletWidth"]
            self.bulletHeight=contents["bulletHeight"]
            self.bulletColor=contents["bulletColor"]
            self.maxBullets=contents["maxBullets"]
            self.fleetDropSpeed=contents["fleetDropSpeed"]
            self.fleetDirection=contents["fleetDirection"]
    
    def levelUp(self):
        self.alienSpeed *= self.nextLevelSpeedFactor
        self.shipSpeed *= self.nextLevelSpeedFactor
        self.bulletSpeed *= self.nextLevelSpeedFactor
        
        self.alienScore *= self.scoreIncreaseFactor
