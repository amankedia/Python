import numpy as np
import matplotlib.pyplot as pp
from pylab import *
x = np.linspace(0,10,40)
sinx = np.sin(x)
cosx = np.cos(x)
ion()
y = sinx * cosx
z = cosx**2 - sinx**2
pp.plot(x,sinx)
pp.plot(x,cosx)
pp.plot(x,y)
pp.plot(x,z)
pp.legend(['sin(x)','cos(x)','sin(x)cos(x)','cos(x)^2-sin(x)^2'])
pp.show()
print(np.dot(sinx,cosx))
print(np.outer(sinx,cosx))
v = np.linspace(0,10,5)
print(v + 1)
vv = np.outer(v,v)
print(vv + v)
print(vv + v[:,np.newaxis])
