import numpy as np
import matplotlib.pyplot as plt
mydata = np.loadtxt('data.txt')
mydata.shape
x = mydata[:,0]
y = mydata[:,1]
line = plt.plot(x,y,'mo')
plt.show()
