import numpy as np
import pylab as plt

xPoints = np.linspace(0,2*np.pi,100)
yPoints = np.linspace(0,2*np.pi,100)

xVary = np.sin(xPoints)
yVary = np.cos(yPoints)
X,Y = np.meshgrid(xPoints,yPoints)

test = xVary[:,None]*yVary[None,:]
test2 = xVary*(xVary[:,None]**2 + yVary[None,:]**2)


plt.contourf(X,Y,test2)
plt.show()
