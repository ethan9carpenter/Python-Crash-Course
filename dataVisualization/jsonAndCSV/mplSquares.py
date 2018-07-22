import matplotlib.pyplot as pyplot

xValues = [i for i in range(1, 6)]
squares = [i*i for i in xValues]
pyplot.plot(xValues, squares, linewidth = 5)

pyplot.title("Square Numbers", fontsize = 24)
pyplot.xlabel("x", fontsize = 12)
pyplot.ylabel("y", fontsize = 12)

pyplot.tick_params(axis = 'both', labelsize = 14)

pyplot.show()


