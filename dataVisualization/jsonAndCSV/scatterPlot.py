import matplotlib.pyplot as pyplot

xVals = list(range(1001))
yVals = [i*i for i in xVals]

#color map to use a color scale
pyplot.scatter(xVals, yVals, s=10, edgecolors=None, c=yVals, cmap=pyplot.cm.Blues)
#pyplot.scatter(xVals, yVals, s = 1, edgecolors=None, c=(0, 0, .8))

pyplot.xlabel("x", fontsize = 11)
pyplot.ylabel("y", fontsize = 11)
pyplot.title("Squared values", fontsize = 26)

pyplot.axis([0, int(1.1 * max(xVals)), 0, int(1.1 * max(yVals))])

pyplot.show()
#pyplot.savefig(<name>.png)
