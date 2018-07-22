from random import randint
import pygal

class Die():
    def __init__(self, numSides=6):
        self.numSides = numSides
    
    def roll(self):
        """Returns the value from a roll of the dice"""
        return randint(1, self.numSides)

rolls = []
die1 = Die()
die2 = Die()

for i in range(1000000):
    rolls.append(die1.roll()*die2.roll())
    
relFrequencies = []
for i in range(1, die1.numSides*die2.numSides+1):
    count = rolls.count(i)
    freq = float(count/len(rolls))
    relFrequencies.append(freq)

histogram = pygal.Bar()
histogram.title = str(len(rolls)) + " rolls of a " + str(die1.numSides) + \
"-Sided Die and a " + str(die2.numSides) + "-Sided Die"

histogram.x_labels = [str(i) for i in range (1, die1.numSides*die2.numSides+1)]
histogram.x_title = "Die Value"
histogram.y_title = "Relative Frequency"

histogram.add(histogram.title, relFrequencies)
histogram.render_to_file("firstGraph.svg")





