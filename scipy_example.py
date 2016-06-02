import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
        '''This returns an array performing e^?? on x where x is the element by 
        element array. a,b,c are constants of the function'''
        return a * np.exp(-b * x) + c
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.2 * np.random.normal(size=len(xdata))
#same as
# ydata =  func(xdata,2.5,2.4,0.5 + 0.2*np.random.normal(size=len(xdata))
#e.g
#ydata = func(xdata * params) * eps

# popt is an array of parameters minimizing the sume of square error
# pcov is the covariance
popt, pcov = curve_fit(func, xdata, ydata)

#perturbed y data
plt.plot(xdata,ydata,marker='*')
# original y data that helpled create perturbed ydata
plt.plot(xdata,y)
#best fit y data to the perturbed data
plt.plot(xdata,func(xdata,popt[0],popt[1],popt[2]), marker = '*')
