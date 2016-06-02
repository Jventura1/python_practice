import numpy as np
mydata = np.loadtxt('data.txt')
import matplotlib.pyplot as plt
mydata.shape
x = mydata[:,0]
y = mydata[:,1]
line = plt.plot(x,y)
