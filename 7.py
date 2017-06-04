#Лаб 3
import pylab
from matplotlib import mlab

def fun(x):
	fun = x**3 - 6*x**2 + 2
	return fun
xMin = 1.1
xMax = 2.9
step = 0.2
xList = mlab.frange(xMin, xMax, step)
yList = [fun (x) for x in xList]
pylab.plot (xList, yList)
pylab.show()
