from random import choice
import matplotlib.pyplot as pyplot

class RandomWalk():
    #Generates random walks
    
    def __init__(self, numPoints = 1000):
        self.numPoints = numPoints
        
        self.xValues = [0]
        self.yValues = [0]
        self.fillWalk()
    
    def fillWalk(self):
        while len(self.xValues) < self.numPoints:
            xDirection = choice([-1, 1])
            xDistance = choice([0, 1, 2, 3, 4])
            xChange = xDistance * xDirection
            
            yDirection = choice([-1, 1])
            yDistance = choice([0, 1, 2, 3, 4])
            yChange = yDistance * yDirection
            
            x = self.xValues[-1] + xChange
            y = self.yValues[-1] + yChange
            
            self.xValues.append(x)
            self.yValues.append(y)
        
walk = RandomWalk(10000)

pointNumbers = list(range(walk.numPoints))

pyplot.figure(figsize=(8, 5), dpi=100)

pyplot.scatter(walk.xValues, walk.yValues, s=1, c=pointNumbers, 
               cmap = pyplot.cm.Reds, edgecolor='none')

pyplot.scatter(walk.xValues[0], walk.yValues[0], s=10, c='green')
pyplot.scatter(walk.xValues[-1], walk.yValues[-1], s=10, c='blue')

'''pyplot.axes().get_xaxis().set_visible(False)
pyplot.axes().get_yaxis().set_visible(False)'''

pyplot.show()

