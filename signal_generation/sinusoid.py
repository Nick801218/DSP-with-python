import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000,endpoint=False)
n = np.arange(1000)  #arange(n)=>array([0 1 2 .... n-1])

x = np.cos(2*np.pi*5*t)
y = np.cos(2*np.pi*5*n/1000)

plt.plot(t,x)
plt.plot(n/1000,y,'--')
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')

plt.show()